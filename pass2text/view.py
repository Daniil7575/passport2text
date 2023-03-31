import PyQt5

from GUI.MainWindow import Ui_MainWindow as Ui_MainWindow
from GUI.SearchWindow import Ui_Dialog as Ui_SearchWindow
from GUI.DeleteWindow import Ui_Dialog as Ui_DeleteWindow
from GUI.FirstPageWindow import Ui_Dialog as Ui_FirstPageWindow
from GUI.SecondPageWindow import Ui_Dialog as Ui_SecondPageWindow
from GUI.SnilsPageWindow import Ui_Dialog as Ui_SnilsWindow

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QDialog, QFileDialog
from db import DB
import sys
from PIL import Image, ImageDraw, ImageEnhance
from PyQt5.QtGui import QPixmap, QImage
import sqlite3
from PyQt5.QtCore import Qt
from Processing import passport_image2dict


IMG_X_PAGE = 591
IMG_Y_PAGE = 711
IMG_X_SNILS = 421
IMG_Y_SNILS = 261

D = {"Код подразделения": "code",
     "Место рождения": "birth_place",
     "Отчество": 'patronymic',
     "Серия": 'series',
     "Номер": 'number',
     "Дата выдачи": 'issue_date',
     "Дата рождения": 'birth_date',
     "Имя": 'name',
     "Фамилия": 'surname',
     "Пол": 'gender',
     "Кем выдан": 'issue_place'}


def check_line(line):
        line = line.strip()
        assert line != ""
        return line

def error_message(error_text):
    error = QMessageBox()
    error.setWindowTitle("Ошибка")
    error.setText(error_text)
    error.setIcon(QMessageBox.Warning)
    error.setStandardButtons(QMessageBox.Ok)
    error.exec_()


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, db: DB):
        super().__init__()  # Инициализация класса
        self.cur = db.cursor
        self.db = db.db
        self.setupUi(self)
        self.button_add.clicked.connect(lambda: self.add_to_db())
        self.button_load.clicked.connect(lambda: self.load_image())
        self.button_search.clicked.connect(lambda: self.search())
        self.button_delete.clicked.connect(lambda: self.delete())
        self.change_table_view()


    def on_enter_click(self):
        self.cur.execute('SELECT * FROM person')
        table = self.cur.fetchall()

        # update table
        for el_index, el in enumerate(table):
            for item_index, item in enumerate(el):
                if str(item) != str(self.table_info.item(el_index, item_index).text()):

                    s = "update person set {column} = '{val}' where series = '{series_val}' and code = '{code_val}' ".\
                        format(
                            column=D[self.table_info.horizontalHeaderItem(
                                item_index).text()],
                            val=self.table_info.item(
                                el_index, item_index).text(),
                            series_val=el[0],
                            code_val=el[1])

                    with open("command.txt", "w") as f:
                        f.write(s)

                    try:
                        self.cur.execute(s)
                        self.conn.commit()
                    except:
                        pass

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            self.on_enter_click()
        if event.key() == Qt.Key_Shift:
            self.change_table_view()

    def search(self):
        window = SearchWindow(self)
        window.exec()

    def delete(self):
        window = DeleteWindow(self)
        window.exec()

    def load_image(self):
        try:
            window = FirstPageWindow(self)
            window.exec()
        except:
            pass

    def add_to_db(self):
        try:
            values = "', '".join(
                ["'" + check_line(self.code.text()),
                check_line(self.birth_place.text()),
                check_line(self.patronymic.text()),
                check_line(self.series.text()),
                check_line(self.number.text()),
                check_line(self.issue_date.text()),
                check_line(self.birth_date.text()),
                check_line(self.name.text()),
                check_line(self.surname.text()),
                check_line(self.gender.text()),
                check_line(self.issue_place.text()) + "'"]
            )
            a = f"""
                INSERT INTO person(
                        code, 
                        birth_place, 
                        patronymic, 
                        series, 
                        number, 
                        issue_date, 
                        birth_date, 
                        name, 
                        surname, 
                        gender, 
                        issue_place
                    ) VALUES({values});
                """
            print(a)
            try:
                self.db.set_trace_callback(print)
                self.cur.execute(a)
            except sqlite3.IntegrityError:
                pass
            self.db.commit()
            self.change_table_view()
        except:
            error_message('Одно или несколько полей не заполнены!')

    def change_table_view(self):
        self.table_info.setRowCount(0)
        self.table_info.clearContents()

        columns = ["Серия", "Номер", "Фамилия", "Имя", "Отчество", "Пол", "Дата рождения",
                   "Место рождения", "Кем выдан", "Дата выдачи", "Код подразделения"]
        self.table_info.setColumnCount(len(columns))
        self.table_info.setHorizontalHeaderLabels(columns)

        self.cur.execute(f'select * from person')

        for eli in self.cur.fetchall():
            rows = self.table_info.rowCount()
            self.table_info.setRowCount(rows + 1)
            for idy, inner_el in enumerate(eli):
                self.table_info.setItem(
                    rows, idy, QTableWidgetItem(str(inner_el)))


class DeleteWindow(QDialog, Ui_DeleteWindow):

    def __init__(self, main_window):
        super().__init__()
        self.setupUi(self)

        self.button_delete.clicked.connect(lambda: self.delete_person())

    def delete_person(self):
        try:
            series = check_line(self.series.text())
            number = check_line(self.number.text())
            print(series, number)
            self.close()
        except:
            error_message('Одно или несколько полей не заполнены!')


class SearchWindow(QDialog, Ui_SearchWindow):

    def __init__(self, main_window):
        super().__init__()
        self.setupUi(self)

        self.button_search.clicked.connect(lambda: self.search_person())

    def search_person(self):
        try:
            series = check_line(self.series.text())
            number = check_line(self.number.text())
            print(series, number)
            self.close()
        except:
            error_message('Одно или несколько полей не заполнены!')
        

class FirstPageWindow(QDialog, Ui_FirstPageWindow):

    def __init__(self, main_window):
        super().__init__()
        self.setupUi(self)
        self.main_window = main_window

        fname = QFileDialog.getOpenFileName(
            self, 'Первая страница паспорта', 'C:\\', "Image files (*.jpg *.png)")
        self.image_path = fname[0]

        image = Image.open(self.image_path)
        w, h = image.width, image.height
        if w > h:
            image = image.rotate(270, expand=True)

        data = passport_image2dict(image)
        self.patronymic.setText('asdasdasd')

        [getattr(self, field_name).setText(value)
         for field_name, value in data.items()]

        image_temp = image.resize((IMG_X_PAGE, IMG_Y_PAGE)).convert('RGBA')
        q = QImage(image_temp.tobytes('raw', 'RGBA'),
                   image_temp.size[0],
                   image_temp.size[1],
                   QImage.Format_RGBA8888)

        pixmap = QPixmap.fromImage(q)
        self.label_image.setPixmap(pixmap)
        self.button_add.clicked.connect(lambda: self.image_parse())

    def image_parse(self):
        try:
            for field_name in D.values():
                getattr(self.main_window, field_name).setText(
                    check_line(getattr(self, field_name).text()))
            try:
                window = SecondPageWindow(self.main_window)
                self.close()
                window.exec()
            except:
                pass
        except:
            error_message('Одно или несколько полей не заполнены!')


class SecondPageWindow(QDialog, Ui_SecondPageWindow):

    def __init__(self, main_window):
        super().__init__()
        self.setupUi(self)
        self.main_window = main_window

        fname = QFileDialog.getOpenFileName(
            self, 'Вторая страница паспорта', 'C:\\', "Image files (*.jpg *.png)")
        self.image_path = fname[0]

        image = Image.open(self.image_path)
        w, h = image.width, image.height
        if w > h:
            image = image.rotate(270, expand=True)
        
        image_temp = image.resize((IMG_X_PAGE, IMG_Y_PAGE)).convert('RGBA')
        q = QImage(image_temp.tobytes('raw', 'RGBA'),
                   image_temp.size[0],
                   image_temp.size[1],
                   QImage.Format_RGBA8888)

        pixmap = QPixmap.fromImage(q)
        self.label_image.setPixmap(pixmap)

        self.button_add.clicked.connect(lambda: self.image_parse())
    
    def image_parse(self):
        try:
            window = SnilsWindow(self.main_window)
            self.close()
            window.exec()
        except:
            pass

class SnilsWindow(QDialog, Ui_SnilsWindow):

    def __init__(self, main_window):
        super().__init__()
        self.setupUi(self)
        self.main_window = main_window

        fname = QFileDialog.getOpenFileName(
            self, 'СНИЛС', 'C:\\', "Image files (*.jpg *.png)")
        self.image_path = fname[0]

        image = Image.open(self.image_path)
        
        image_temp = image.resize((IMG_X_SNILS, IMG_Y_SNILS)).convert('RGBA')
        q = QImage(image_temp.tobytes('raw', 'RGBA'),
                   image_temp.size[0],
                   image_temp.size[1],
                   QImage.Format_RGBA8888)

        pixmap = QPixmap.fromImage(q)
        self.label_image.setPixmap(pixmap)

        self.button_add.clicked.connect(lambda: self.image_parse())

    def image_parse(self):
        self.close()