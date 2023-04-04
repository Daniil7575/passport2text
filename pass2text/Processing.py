import pytesseract
from typing import Union, Dict
import re
from PIL import Image, ImageDraw

ERROR_TAG = '-'
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\spovt\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# ПОМЕНЯЙТЕ ПУТЬ НА ВАЛИДНЫЙ ДО ТЕССЕРАКТА!


def _ocr_core(filename: Union[Image.Image, str]):
    image = Image.open(filename) if isinstance(filename, str) else filename
    draw = ImageDraw.Draw(image)  # Создаем инструмент для рисования.
    width = image.size[0]  # Определяем ширину.
    height = image.size[1]  # Определяем высоту.
    pix = image.load()
    for i in range(width):
        for j in range(height):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            if a > 220:
                a, b, c = 255, 255, 255
            draw.point((i, j), (a, b, c))
    for i in range(width):
        for j in range(height):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            S = a + b + c
            if (S > (((255 + 80) // 3) * 3)):  # 80 3 3
                a, b, c = 255, 255, 255
            else:
                a, b, c = 0, 0, 0
            draw.point((i, j), (a, b, c))
    # enh = ImageEnhance.Brightness(image)


def get_first_match(regex_list: list) -> Union[str, None]:
    if regex_list:
        return regex_list[0]
    return ERROR_TAG

def get_at_index(lst: list, idx: int) -> str:
    if len(lst) > idx:
        return lst[idx]
    return ERROR_TAG

def passport_image2dict(image: Union[Image.Image, str],
                        show_images: bool = False,
                        print_output: bool = True) -> Dict[str, str]:
    image = Image.open(image) if isinstance(image, str) else image
    w, h = image.width, image.height
    if w > h:
        image = image.rotate(270, expand=True)
    w, h = image.width, image.height
    # верхняя часть
    image1 = image.crop((0, h*0.09, w*0.895, h*0.255))
    _ocr_core(image1)
    # нижняя часть
    image2 = image.crop((w*0.4, h*0.55, w*0.895, h*0.85))
    _ocr_core(image2)
    # серия номер
    image3 = image.crop((w*0.895, h*0.12, w*0.95, h*0.5))
    image3 = image3.rotate(90, expand=True)
    # ocr_core(image3)
    if show_images:
        image1.show()
        image2.show()
        image3.show()

    # --------------------Верхняя часть---------------------------------------
    upper_section = pytesseract.image_to_string(image1, lang="rus")
    date_r = r'\d\d\.\d\d\.\d{4}'
    whom_unit_number = re.split(date_r, upper_section)
    whom = ' '.join(get_at_index(whom_unit_number, 0).replace('\n', ' ').split())
    whom = get_first_match(re.findall(r'[А-Я.]+ (?:[А-Я. -]+|[№\d ]+)+', whom))
    date_of_issue = get_first_match(re.findall(date_r, upper_section))
    # whom_unit_number[1]
    code = get_first_match(re.findall(r"[0-9]{3}-[0-9]{3}", get_at_index(whom_unit_number, 1)))

    # --------------------Верхняя часть---------------------------------------

    # --------------------Нижняя часть---------------------------------------
    down_section = pytesseract.image_to_string(image2, lang='rus')
    fio_sex_born = re.split(date_r, down_section)
    patronymic_r = r'[А-Я]+(?:ОВИЧ|ЕВИЧ|ОВНА|ИЧНА|ЕВНА|ИНИЧНА)'

    fio_sex = ' '.join((fio_sex_born[0]).replace('\n', ' ').split())
    try:
        fi, sex = re.split(patronymic_r, fio_sex)
    except:
        fi, sex = ERROR_TAG, ERROR_TAG
    fio_r = r'(?:[А-Я]{3,}\b)'  # Длина слов > 3
    fi = re.findall(fio_r, fi)
    try:
        surname = fi[0]
        name = fi[1]

    except IndexError:
        surname = ERROR_TAG
        name = ERROR_TAG

    o = re.findall(patronymic_r, fio_sex)

    sex = 'МУЖ.' if re.findall(r'(?:М|[МУ]+|УЖ|Ж\.)', sex) else 'ЖЕН.'

    born_date = get_first_match(re.findall(date_r, down_section))

    born = ' '.join(get_at_index(fio_sex_born, 1).replace('\n', ' ').split())
    # --------------------Нижняя часть----------------------------------------

    # --------------------Серия номер-----------------------------------------
    series_number = pytesseract.image_to_string(image3, lang="rus")

    series = get_first_match(re.findall(r'\d\d \d\d\b', series_number))


    number = get_first_match(re.findall(r'\d{6}', series_number))

    # --------------------Серия номер----------------------------------------

    if print_output:
        print(f'Кем выдан: {whom}')
        print(f'Дата выдачи: {date_of_issue}')
        print(f'Код подразделения: {code}')
        print(f'Фамилия: {surname}')
        print(f'Имя: {name}')
        print(f'Отчество: {get_first_match(o)}')
        print(f'Пол: {sex}')
        print(f'Дата рождения: {born_date}')
        print(f'Место рождения: {born}')
        print(f'Серия: {series}')
        print(f'Номер: {number}', end='\n\n')

    return {
        'issue_place': whom,
        'issue_date': date_of_issue,
        'code1': code,
        'surname': surname,
        'name': name,
        'patronymic': get_first_match(o),
        'gender': sex,
        'birth_date': born_date,
        'birth_place': born,
        'series': series,
        'number': number
    }


def passport_second_page_image2dict(
        image: Union[Image.Image, str],
        show_images: bool = False,
        print_output: bool = True) -> Dict[str, str]:
    image = Image.open(image) if isinstance(image, str) else image
    w, h = image.width, image.height
    if w < h:
        image = image.rotate(90, expand=True)
    w, h = image.width, image.height
    image = image.crop((w * 0.51, 0, w, h * 0.5))
    image1 = image
    
    w, h = image.width, image.height
    image1 = image1.crop((w * 0.19, h * 0.28, w * 0.8, h * 0.56))
    # image1.show()
    series_number = pytesseract.image_to_string(image1, lang="rus")

    region_r = r'[А-Я ]* ?ОБЛ\.? ?[А-Я ]*'
    district_r = r'^[Р\-Н ]*[А-Я]+$'
    city_r = r'(?:(?:ПОС\. ){1}|(?:ГОР\. ){1})[ А-Я]+'
    street_r = r'[А-Я ]* ?УЛ\.? ?[А-Я ]*'
    building_r = r'(?:\d+ ?[А-я:\- \.]*)+'

    second_page = {
        'region': get_first_match(re.findall(region_r, series_number)),
        'ray': get_first_match(re.findall(district_r, series_number)),
        'punkt': get_first_match(re.findall(city_r, series_number)),
        'street': get_first_match(re.findall(street_r, series_number)),
        'house': get_first_match(re.findall(building_r, series_number))
    }

    image2 = image.crop((w * 0.15, h * 0.23, w * 0.8, h * 0.31))
    date = pytesseract.image_to_string(image2, lang="rus")
    second_page['reg_date'] = date.strip() if date.strip() else ERROR_TAG
    image3 = image.crop((w * 0.18, h * 0.57, w * 0.91, h * 0.7))
    department = pytesseract.image_to_string(image3, lang="rus").strip()
    second_page['state'] = department if department.strip() else ERROR_TAG
    if show_images:
        image1.show()
        image2.show()
        image3.show()
    print(second_page)
    # image1.show()
    # image2.show()
    # image3.show()
    return second_page


def snils_image2dict(image: Union[Image.Image, str],
                     show_images: bool = False,
                     print_output: bool = True) -> Dict[str, str]:
    image = Image.open(image) if isinstance(image, str) else image
    w, h = image.width, image.height

    if w < h:
        image = image.rotate(270, expand=True)

    print(image.width, image.height)
    image = image.crop((0, h * 0.28, w, h * 0.399))

    # if show_images:
    #     image.show()

    # snils_number_r = r'\d+[-]\d+[-]\d+[ ]\d+'
    # snils_capture = pytesseract.image_to_string(image, lang="rus")

    # snils = {
    #     'snils': get_first_match(re.findall(snils_number_r, snils_capture)).strip()
    # }
    # print(snils)
    # return snils


if __name__ == '__main__':
    # for i in range(1, 9):
    #     snils_image2dict(f'C:\\Users\\spovt\\Desktop\\kadrovik\\pass2text\\pass2text\\test\\snils\\{i}.jpg', True)
    for i in range(1, 14):
        passport_second_page_image2dict(f'C:\\Users\\spovt\\Desktop\\kadrovik\\pass2text\\pass2text\\test\\2pg\\{i}.jpg', True)

    # snils_image2dict(f'C:\\Users\\spovt\\Desktop\\kadrovik\\pass2text\\pass2text\\test\\snils\\5.jpg', True)
    # passport_second_page_image2dict(
    #     'C:\\Users\\spovt\\Desktop\\kadrovik\\pass2text\\test_photos\\second_page\\5.jpg', True)
