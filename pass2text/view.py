import PyQt5
import MW
from PyQt5 import QtWidgets  # Основной файл программы с прописанной логикой
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem # Импортирование необходимых виджетов из библиотеки PyQt5
from Processing import passport_image2dict
from db import DB
import sys
import sqlite3
from PyQt5.QtCore import Qt

D = {"Код подразделения" : "code" ,
    "Место рождения" : "birth_place" , 
    "Отчество" : 'patronymic', 
    "Серия" : 'series', 
    "Номер" : 'number', 
    "Дата выдачи" : 'issue_date', 
    "Дата рождения" : 'birth_date', 
    "Имя" : 'name', 
    "Фамилия" : 'surname', 
    "Пол" : 'gender', 
    "Кем выдан" : 'issue_place'}


class MainWindow(QMainWindow, MW.Ui_MainWindow):  # Объявление класса Калькулятор, который наследуется от QMainWindow, в котором прописан весь основной интерфейс программы (интерфейс создан в программе QtDesigner)
    def __init__(self, db: DB):
        super().__init__()  # Инициализация класса
        self.cur = db.cursor
        self.db = db.db
        self.setupUi(self)
        self.add_functions()
        self.change_table_view()
    
    def add_functions(self):
        self.button_add.clicked.connect(lambda: self.add_to_db())
    
    def on_enter_click(self):
        self.cur.execute('SELECT * FROM person')
        table = self.cur.fetchall()

        # update table
        for el_index, el in enumerate(table):
            for item_index, item in enumerate(el):
                if str(item) != str(self.table_info.item(el_index, item_index).text()):

                    s = "update person set {column} = '{val}' where series = '{series_val}' and code = '{code_val}' ".\
                        format( 
                        column = D[self.table_info.horizontalHeaderItem(item_index).text()], 
                        val = self.table_info.item(el_index, item_index).text(),  
                        series_val = el[0], 
                        code_val = el[1])
                    
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
    
    def add_to_db(self):
        values = ", ".join(
            [self.code.text(),
            self.birth_place.text(),
            self.patronymic.text(),
            self.series.text(),
            self.number.text(),
            self.issue_date.text(),
            self.birth_date.text(),
            self.name.text(),
            self.surname.text(),
            self.gender.text(),
            self.issue_place.text()]
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
        try:
            self.cur.execute(a)
        except sqlite3.IntegrityError:
            pass
        self.db.commit()
        self.change_table_view()
    
    def change_table_view(self):
        self.table_info.setRowCount(0)
        self.table_info.clearContents()

        columns = ["Серия", "Номер", "Фамилия", "Имя", "Отчество", "Пол", "Дата рождения", "Место рождения", "Кем выдан", "Дата выдачи", "Код подразделения"]
        self.table_info.setColumnCount(len(columns))
        self.table_info.setHorizontalHeaderLabels(columns)

        self.cur.execute(f'select * from person')

        for eli in self.cur.fetchall():
            rows = self.table_info.rowCount()
            self.table_info.setRowCount(rows + 1)
            for idy, inner_el in enumerate(eli):
                self.table_info.setItem(rows, idy, QTableWidgetItem(str(inner_el)))
