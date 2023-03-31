import PyQt5

from GUI.MainWindow import Ui_MainWindow as Ui_MainWindow
from GUI.SearchWindow import Ui_Dialog as Ui_SearchWindow
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


IMG_X = 410
IMG_Y = 520

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


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, db: DB):
        super().__init__()  # Инициализация класса
        self.cur = db.cursor
        self.db = db.db
        self.setupUi(self)
        self.button_add.clicked.connect(lambda: self.add_to_db())
        self.button_load.clicked.connect(lambda: self.load_image())
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

    def load_image(self):
        window = FirstPageWindow(self)
        window.exec()

    def add_to_db(self):
        values = "', '".join(
            ["'" + self.code.text(),
             self.birth_place.text(),
             self.patronymic.text(),
             self.series.text(),
             self.number.text(),
             self.issue_date.text(),
             self.birth_date.text(),
             self.name.text(),
             self.surname.text(),
             self.gender.text(),
             self.issue_place.text() + "'"]
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


class SearchWindow(QDialog, Ui_SearchWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)


class FirstPageWindow(QDialog, Ui_FirstPageWindow):

    def __init__(self, main_window):
        super().__init__()  # Инициализация класса
        self.setupUi(self)
        self.main_window = main_window

        fname = QFileDialog.getOpenFileName(
            self, 'Первая страница паспорта', 'C:\\', "Image files (*.jpg *.png)")
        self.image_path = fname[0]
        print(self.image_path)

        image = Image.open(self.image_path)
        w, h = image.width, image.height
        if w > h:
            image = image.rotate(270, expand=True)

        data = passport_image2dict(image)
        self.patronymic.setText('asdasdasd')

        [getattr(self, field_name).setText(value)
         for field_name, value in data.items()]

        image_temp = image.resize((IMG_X, IMG_Y)).convert('RGBA')
        q = QImage(image_temp.tobytes('raw', 'RGBA'),
                   image_temp.size[0],
                   image_temp.size[1],
                   QImage.Format_RGBA8888)

        pixmap = QPixmap.fromImage(q)
        self.label_image.setPixmap(pixmap)
        self.button_add.clicked.connect(lambda: self.image_parse())

    def image_parse(self):
        for field_name in D.values():
            getattr(self.main_window, field_name).setText(
                getattr(self, field_name).text())

        self.close()


class SecondPageWindow(QDialog, Ui_SecondPageWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)


class SnilsWindow(QDialog, Ui_SnilsWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)