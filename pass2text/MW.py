# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MW.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(871, 601)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_surname = QtWidgets.QLabel(self.centralwidget)
        self.label_surname.setGeometry(QtCore.QRect(30, 20, 161, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        self.label_surname.setFont(font)
        self.label_surname.setObjectName("label_surname")
        self.label_name = QtWidgets.QLabel(self.centralwidget)
        self.label_name.setGeometry(QtCore.QRect(240, 20, 161, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        self.label_name.setFont(font)
        self.label_name.setObjectName("label_name")
        self.label_patronymic = QtWidgets.QLabel(self.centralwidget)
        self.label_patronymic.setGeometry(QtCore.QRect(450, 20, 161, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        self.label_patronymic.setFont(font)
        self.label_patronymic.setObjectName("label_patronymic")
        self.label_birth_date = QtWidgets.QLabel(self.centralwidget)
        self.label_birth_date.setGeometry(QtCore.QRect(240, 100, 151, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        self.label_birth_date.setFont(font)
        self.label_birth_date.setObjectName("label_birth_date")
        self.label_birth_place = QtWidgets.QLabel(self.centralwidget)
        self.label_birth_place.setGeometry(QtCore.QRect(450, 100, 161, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        self.label_birth_place.setFont(font)
        self.label_birth_place.setObjectName("label_birth_place")
        self.label_code = QtWidgets.QLabel(self.centralwidget)
        self.label_code.setGeometry(QtCore.QRect(450, 180, 191, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        self.label_code.setFont(font)
        self.label_code.setObjectName("label_code")
        self.label_gender = QtWidgets.QLabel(self.centralwidget)
        self.label_gender.setGeometry(QtCore.QRect(30, 100, 161, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        self.label_gender.setFont(font)
        self.label_gender.setObjectName("label_gender")
        self.label_series = QtWidgets.QLabel(self.centralwidget)
        self.label_series.setGeometry(QtCore.QRect(660, 20, 121, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        self.label_series.setFont(font)
        self.label_series.setObjectName("label_series")
        self.label_issue_place = QtWidgets.QLabel(self.centralwidget)
        self.label_issue_place.setGeometry(QtCore.QRect(30, 180, 121, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        self.label_issue_place.setFont(font)
        self.label_issue_place.setObjectName("label_issue_place")
        self.label_issue_date = QtWidgets.QLabel(self.centralwidget)
        self.label_issue_date.setGeometry(QtCore.QRect(240, 180, 131, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        self.label_issue_date.setFont(font)
        self.label_issue_date.setObjectName("label_issue_date")
        self.label_number = QtWidgets.QLabel(self.centralwidget)
        self.label_number.setGeometry(QtCore.QRect(660, 100, 121, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        self.label_number.setFont(font)
        self.label_number.setObjectName("label_number")
        self.table_info = QtWidgets.QTableWidget(self.centralwidget)
        self.table_info.setGeometry(QtCore.QRect(30, 280, 811, 291))
        self.table_info.setObjectName("table_info")
        self.table_info.setColumnCount(11)
        self.table_info.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_info.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_info.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_info.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_info.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_info.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_info.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_info.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_info.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_info.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_info.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_info.setHorizontalHeaderItem(10, item)
        self.button_load = QtWidgets.QPushButton(self.centralwidget)
        self.button_load.setGeometry(QtCore.QRect(660, 230, 181, 31))
        self.button_load.setObjectName("button_load")
        self.button_add = QtWidgets.QPushButton(self.centralwidget)
        self.button_add.setGeometry(QtCore.QRect(660, 190, 181, 31))
        self.button_add.setObjectName("button_add")
        self.code = QtWidgets.QLineEdit(self.centralwidget)
        self.code.setGeometry(QtCore.QRect(450, 220, 181, 31))
        self.code.setObjectName("code")
        self.birth_place = QtWidgets.QLineEdit(self.centralwidget)
        self.birth_place.setGeometry(QtCore.QRect(450, 140, 181, 31))
        self.birth_place.setObjectName("birth_place")
        self.patronymic = QtWidgets.QLineEdit(self.centralwidget)
        self.patronymic.setGeometry(QtCore.QRect(450, 60, 181, 31))
        self.patronymic.setObjectName("patronymic")
        self.series = QtWidgets.QLineEdit(self.centralwidget)
        self.series.setGeometry(QtCore.QRect(660, 60, 181, 31))
        self.series.setObjectName("series")
        self.number = QtWidgets.QLineEdit(self.centralwidget)
        self.number.setGeometry(QtCore.QRect(660, 140, 181, 31))
        self.number.setObjectName("number")
        self.issue_date = QtWidgets.QLineEdit(self.centralwidget)
        self.issue_date.setGeometry(QtCore.QRect(240, 220, 181, 31))
        self.issue_date.setObjectName("issue_date")
        self.birth_date = QtWidgets.QLineEdit(self.centralwidget)
        self.birth_date.setGeometry(QtCore.QRect(240, 140, 181, 31))
        self.birth_date.setObjectName("birth_date")
        self.name = QtWidgets.QLineEdit(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(240, 60, 181, 31))
        self.name.setObjectName("name")
        self.surname = QtWidgets.QLineEdit(self.centralwidget)
        self.surname.setGeometry(QtCore.QRect(30, 60, 181, 31))
        self.surname.setObjectName("surname")
        self.gender = QtWidgets.QLineEdit(self.centralwidget)
        self.gender.setGeometry(QtCore.QRect(30, 140, 181, 31))
        self.gender.setObjectName("gender")
        self.issue_place = QtWidgets.QLineEdit(self.centralwidget)
        self.issue_place.setGeometry(QtCore.QRect(30, 220, 181, 31))
        self.issue_place.setObjectName("issue_place")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Глаавное окно"))
        self.label_surname.setText(_translate("MainWindow", "Фамилия"))
        self.label_name.setText(_translate("MainWindow", "Имя"))
        self.label_patronymic.setText(_translate("MainWindow", "Отчество"))
        self.label_birth_date.setText(_translate("MainWindow", "Дата рождения"))
        self.label_birth_place.setText(_translate("MainWindow", "Место рождения"))
        self.label_code.setText(_translate("MainWindow", "Код подразделения"))
        self.label_gender.setText(_translate("MainWindow", "Пол"))
        self.label_series.setText(_translate("MainWindow", "Серия"))
        self.label_issue_place.setText(_translate("MainWindow", "Кем выдан"))
        self.label_issue_date.setText(_translate("MainWindow", "Дата выдачи"))
        self.label_number.setText(_translate("MainWindow", "Номер"))
        item = self.table_info.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Серия"))
        item = self.table_info.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Номер"))
        item = self.table_info.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Фамилия"))
        item = self.table_info.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Имя"))
        item = self.table_info.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Отчество"))
        item = self.table_info.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Пол"))
        item = self.table_info.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Дата рождения"))
        item = self.table_info.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Место рождения"))
        item = self.table_info.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Кем выдан"))
        item = self.table_info.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Дата выдачи"))
        item = self.table_info.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "Код подразделения"))
        self.button_load.setText(_translate("MainWindow", "Добавить по фото"))
        self.button_add.setText(_translate("MainWindow", "Добавить"))