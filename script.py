from PIL import Image, ImageDraw, ImageEnhance
import pytesseract
from typing import Union, Dict
import os
import re
from PIL import Image, ImageDraw


ERROR_TAG = '[НЕ РАСПОЗНАНО]'
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR'


def ocr_core(filename: Union[Image.Image, str]):
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
        # for i in range(width):
        #     for j in range(height):
        #         a = pix[i, j][0] + 10
        #         b = pix[i, j][1] + 10
        #         c = pix[i, j][2] + 10
        #         if (a < 0):
        #             a = 0
        #         if (b < 0):
        #             b = 0
        #         if (c < 0):
        #             c = 0
        #         if (a > 255):
        #             a = 255
        #         if (b > 255):
        #             b = 255
        #         if (c > 255):
        #             c = 255
        #         draw.point((i, j), (a, b, c))
        enh = ImageEnhance.Brightness(image)


# If you don't have tesseract executable in your PATH, include the following:

# Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'


def passport_image2dict(image: Union[Image.Image, str], show_images: bool = False, print_output: bool = True) -> Dict[str, str]:
    image = Image.open(image) if isinstance(image, str) else image
    w, h = image.width, image.height
    if w > h:
        image = image.rotate(270, expand=True)
    w, h = image.width, image.height
    # верхняя часть
    image1 = image.crop((0, h*0.09, w*0.895, h*0.255))
    ocr_core(image1)
    # нижняя часть
    image2 = image.crop((w*0.4, h*0.55, w*0.895,h*0.85))
    ocr_core(image2)
    # серия номер
    image3 = image.crop((w*0.895, h*0.12, w*0.95, h*0.5))
    image3 = image3.rotate(90, expand=True)
    # ocr_core(image3)
    if show_images:
        image1.show()
        image2.show()
        image3.show()

    # --------------------Верхняя часть----------------------------------------------
    upper_section = pytesseract.image_to_string(image1, lang="rus")
    date_r = r'\d\d\.\d\d\.\d{4}'
    whom_unit_number = re.split(date_r, upper_section)
    whom = ' '.join(whom_unit_number[0].replace('\n', ' ').split())
    whom = re.findall(r'[А-Я.]+ (?:[А-Я. -]+|[№\d ]+)+', whom)[0]
    date_of_issue = re.findall(date_r, upper_section)[0]
    code = re.findall(r"[0-9]{3}-[0-9]{3}", whom_unit_number[1])[0]

    # --------------------Верхняя часть----------------------------------------------

    # --------------------Нижняя часть-----------------------------------------------    
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
    # --------------------Нижняя часть----------------------------------------------

    # --------------------Серия номер-----------------------------------------------
    series_number = pytesseract.image_to_string(image3, lang="rus")
    try:
        series = re.findall(r'\d\d \d\d\b', series_number)[0]
    except IndexError:
        series = ERROR_TAG
    try:
        number = re.findall(r'\d{6}', series_number)[0]
    except IndexError:
        number = ERROR_TAG
    # --------------------Серия номер-----------------------------------------------

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
        'Кем выдан': whom,
        'Дата выдачи': date_of_issue,
        'Код подразделения': code,
        'Фамилия': surname,
        'Имя': name,
        'Отчество': o[0],
        'Пол': sex,
        'Дата рождения': born_date,
        'Место рождения': born,
        'Серия': series,
        'Номер': number
    }


photos = '\\test_photos\\'
directory = os.getcwd() + photos

for filename in os.listdir(directory):
    passport_image2dict(directory + filename)

