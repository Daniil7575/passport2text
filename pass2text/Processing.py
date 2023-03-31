import pytesseract
from typing import Union, Dict
import re
from PIL import Image, ImageDraw


# pytesseract.pytesseract.tesseract_cmd =
# r'C:\Users\spovt\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

IMAGE_NAME = "temp2.png"
ERROR_TAG = '[НЕ РАСПОЗНАНО]'
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\spovt\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'


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


# If you don't have tesseract executable in your PATH, include the following:

# Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'


def get_first_match(regex_list: list) -> Union[str, None]:
    if regex_list:
        return regex_list[0]
    return ''


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
    whom = ' '.join(whom_unit_number[0].replace('\n', ' ').split())
    whom = re.findall(r'[А-Я.]+ (?:[А-Я. -]+|[№\d ]+)+', whom)[0]
    date_of_issue = re.findall(date_r, upper_section)[0]
    code = re.findall(r"[0-9]{3}-[0-9]{3}", whom_unit_number[1])[0]

    # --------------------Верхняя часть---------------------------------------

    # --------------------Нижняя часть---------------------------------------
    down_section = pytesseract.image_to_string(image2, lang='rus')
    fio_sex_born = re.split(date_r, down_section)
    patronymic_r = r'[А-Я]+(?:ОВИЧ|ЕВИЧ|ОВНА|ИЧНА|ЕВНА|ИНИЧНА)'

    fio_sex = ' '.join(fio_sex_born[0].replace('\n', ' ').split())
    fi, sex = re.split(patronymic_r, fio_sex)
    fio_r = r'(?:[А-Я]{3,}\b)'  # Длина слов > 3
    fi = re.findall(fio_r, fi)
    try:
        surname = fi[0]
        name = fi[1]

    except IndexError:
        name = ERROR_TAG

    o = re.findall(patronymic_r, fio_sex)

    sex = 'МУЖ.' if re.findall(r'(?:М|[МУ]+|УЖ|Ж\.)', sex) else 'ЖЕН.'

    born_date = re.findall(date_r, down_section)[0]

    born = ' '.join(fio_sex_born[1].replace('\n', ' ').split())
    # --------------------Нижняя часть----------------------------------------

    # --------------------Серия номер-----------------------------------------
    series_number = pytesseract.image_to_string(image3, lang="rus")
    try:
        series = re.findall(r'\d\d \d\d\b', series_number)[0]
    except IndexError:
        series = ERROR_TAG
    try:
        number = re.findall(r'\d{6}', series_number)[0]
    except IndexError:
        number = ERROR_TAG
    # --------------------Серия номер----------------------------------------

    if print_output:
        print(f'Кем выдан: {whom}')
        print(f'Дата выдачи: {date_of_issue}')
        print(f'Код подразделения: {code}')
        print(f'Фамилия: {surname}')
        print(f'Имя: {name}')
        print(f'Отчество: {o[0]}')
        print(f'Пол: {sex}')
        print(f'Дата рождения: {born_date}')
        print(f'Место рождения: {born}')
        print(f'Серия: {series}')
        print(f'Номер: {number}', end='\n\n')

    return {
        'issue_place': whom,
        'issue_date': date_of_issue,
        'code': code,
        'surname': surname,
        'name': name,
        'patronymic': o[0],
        'gender': sex,
        'birth_date': born_date,
        'birth_place': born,
        'series': series,
        'number': number
    }


def passport_second_page_image2dict(image: Union[Image.Image, str],
                         show_images: bool = False,
                         print_output: bool = True) -> Dict[str, str]:
    image = Image.open(image) if isinstance(image, str) else image
    w, h = image.width, image.height
    if w < h:
        image = image.rotate(270, expand=True)
    w, h = image.width, image.height
    image = image.crop((w * 0.51, 0, w, h * 0.5))
    image1 = image
    # if show_images:
    # image1.show()
    w, h = image.width, image.height
    image1 = image1.crop((w * 0.19, h * 0.28, w * 0.8, h * 0.56))
    series_number = pytesseract.image_to_string(image1, lang="rus")

    region_r = r'[А-Я ]* ?ОБЛ\.? ?[А-Я ]*'
    district_r = r'^[Р\-Н ]*[А-Я]+$'
    city_r = r'(?:(?:ПОС\. ){1}|(?:ГОР\. ){1})[ А-Я]+'
    street_r = r'[А-Я ]* ?УЛ\.? ?[А-Я ]*'
    building_r = r'(?:\d+ ?[А-я:\- \.]*)+'

    second_page = {
        'region': get_first_match(re.findall(region_r, series_number)),
        'district': get_first_match(re.findall(district_r, series_number)),
        'city': get_first_match(re.findall(city_r, series_number)),
        'street': get_first_match(re.findall(street_r, series_number)),
        'building': get_first_match(re.findall(building_r, series_number))
    }

    image2 = image.crop((w * 0.20, h * 0.23, w * 0.8, h * 0.31))
    date = pytesseract.image_to_string(image2, lang="rus")
    second_page['date'] = date.strip()
    image3 = image.crop((w * 0.16, h * 0.53, w * 0.89, h * 0.74))
    department = pytesseract.image_to_string(image3, lang="rus").strip()
    second_page['department'] = department
    print(second_page)
    # image1.show()
    # image2.show()
    # image3.show()
    return second_page
    # print(second_page)
    # if show_images:


def snils_image2dict(image: Union[Image.Image, str],
                     show_images: bool = False,
                     print_output: bool = True) -> Dict[str, str]:
    image = Image.open(image) if isinstance(image, str) else image
    w, h = image.width, image.height
    if w < h:
        image = image.rotate(270, expand=True)
    image = image.crop((0, h * 0.28, w, h * 0.38))

    if show_images:
        image.show()

    snils_number_r = r'[0-9\- ]+\b'
    snils_capture = pytesseract.image_to_string(image, lang="rus")

    snils = {
        'snils': get_first_match(re.findall(snils_number_r, snils_capture)).strip()
    }
    # print(snils)
    return snils


if __name__ == '__main__':
    snils_image2dict('C:\\Users\\spovt\\Desktop\\kadrovik\\pass2text\\test_photos\\snils\\_20110331_13253405.jpg', True)
    # passport_second_page_image2dict(
    # 'C:\\Users\\spovt\\Desktop\\kadrovik\\pass2text\\test_photos\\second_page\\2.jpg', True)
