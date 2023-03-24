# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1255, 1532)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_name = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        self.label_name.setFont(font)
        self.label_name.setAlignment(QtCore.Qt.AlignCenter)
        self.label_name.setObjectName("label_name")
        self.verticalLayout_2.addWidget(self.label_name)
        self.name = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.name.setFont(font)
        self.name.setObjectName("name")
        self.verticalLayout_2.addWidget(self.name)
        self.label_surname = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        self.label_surname.setFont(font)
        self.label_surname.setAlignment(QtCore.Qt.AlignCenter)
        self.label_surname.setObjectName("label_surname")
        self.verticalLayout_2.addWidget(self.label_surname)
        self.surname = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.surname.setFont(font)
        self.surname.setObjectName("surname")
        self.verticalLayout_2.addWidget(self.surname)
        self.label_patronymic = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        self.label_patronymic.setFont(font)
        self.label_patronymic.setAlignment(QtCore.Qt.AlignCenter)
        self.label_patronymic.setObjectName("label_patronymic")
        self.verticalLayout_2.addWidget(self.label_patronymic)
        self.patronymic = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.patronymic.setFont(font)
        self.patronymic.setObjectName("patronymic")
        self.verticalLayout_2.addWidget(self.patronymic)
        self.label_series = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        self.label_series.setFont(font)
        self.label_series.setAlignment(QtCore.Qt.AlignCenter)
        self.label_series.setObjectName("label_series")
        self.verticalLayout_2.addWidget(self.label_series)
        self.series = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.series.setFont(font)
        self.series.setObjectName("series")
        self.verticalLayout_2.addWidget(self.series)
        self.label_number = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        self.label_number.setFont(font)
        self.label_number.setAlignment(QtCore.Qt.AlignCenter)
        self.label_number.setObjectName("label_number")
        self.verticalLayout_2.addWidget(self.label_number)
        self.number = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.number.setFont(font)
        self.number.setObjectName("number")
        self.verticalLayout_2.addWidget(self.number)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_gender = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        self.label_gender.setFont(font)
        self.label_gender.setAlignment(QtCore.Qt.AlignCenter)
        self.label_gender.setObjectName("label_gender")
        self.verticalLayout_4.addWidget(self.label_gender)
        self.gender = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.gender.setFont(font)
        self.gender.setObjectName("gender")
        self.verticalLayout_4.addWidget(self.gender)
        self.label_birth_date = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        self.label_birth_date.setFont(font)
        self.label_birth_date.setAlignment(QtCore.Qt.AlignCenter)
        self.label_birth_date.setObjectName("label_birth_date")
        self.verticalLayout_4.addWidget(self.label_birth_date)
        self.birth_date = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.birth_date.setFont(font)
        self.birth_date.setObjectName("birth_date")
        self.verticalLayout_4.addWidget(self.birth_date)
        self.label_birth_place = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        self.label_birth_place.setFont(font)
        self.label_birth_place.setAlignment(QtCore.Qt.AlignCenter)
        self.label_birth_place.setObjectName("label_birth_place")
        self.verticalLayout_4.addWidget(self.label_birth_place)
        self.birth_place = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.birth_place.setFont(font)
        self.birth_place.setObjectName("birth_place")
        self.verticalLayout_4.addWidget(self.birth_place)
        self.label_issue_place = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        self.label_issue_place.setFont(font)
        self.label_issue_place.setAlignment(QtCore.Qt.AlignCenter)
        self.label_issue_place.setObjectName("label_issue_place")
        self.verticalLayout_4.addWidget(self.label_issue_place)
        self.issue_place = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.issue_place.setFont(font)
        self.issue_place.setObjectName("issue_place")
        self.verticalLayout_4.addWidget(self.issue_place)
        self.label_issue_date = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        self.label_issue_date.setFont(font)
        self.label_issue_date.setAlignment(QtCore.Qt.AlignCenter)
        self.label_issue_date.setObjectName("label_issue_date")
        self.verticalLayout_4.addWidget(self.label_issue_date)
        self.issue_date = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.issue_date.setFont(font)
        self.issue_date.setObjectName("issue_date")
        self.verticalLayout_4.addWidget(self.issue_date)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_code = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        self.label_code.setFont(font)
        self.label_code.setAlignment(QtCore.Qt.AlignCenter)
        self.label_code.setObjectName("label_code")
        self.verticalLayout_5.addWidget(self.label_code)
        self.code = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.code.setFont(font)
        self.code.setObjectName("code")
        self.verticalLayout_5.addWidget(self.code)
        self.label_reg_date = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_reg_date.setFont(font)
        self.label_reg_date.setAlignment(QtCore.Qt.AlignCenter)
        self.label_reg_date.setObjectName("label_reg_date")
        self.verticalLayout_5.addWidget(self.label_reg_date)
        self.reg_date = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.reg_date.setFont(font)
        self.reg_date.setObjectName("reg_date")
        self.verticalLayout_5.addWidget(self.reg_date)
        self.label_region = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_region.setFont(font)
        self.label_region.setAlignment(QtCore.Qt.AlignCenter)
        self.label_region.setObjectName("label_region")
        self.verticalLayout_5.addWidget(self.label_region)
        self.region = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.region.setFont(font)
        self.region.setObjectName("region")
        self.verticalLayout_5.addWidget(self.region)
        self.label_ray = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_ray.setFont(font)
        self.label_ray.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ray.setObjectName("label_ray")
        self.verticalLayout_5.addWidget(self.label_ray)
        self.ray = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ray.setFont(font)
        self.ray.setObjectName("ray")
        self.verticalLayout_5.addWidget(self.ray)
        self.label_punkt = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_punkt.setFont(font)
        self.label_punkt.setAlignment(QtCore.Qt.AlignCenter)
        self.label_punkt.setObjectName("label_punkt")
        self.verticalLayout_5.addWidget(self.label_punkt)
        self.punkt = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.punkt.setFont(font)
        self.punkt.setObjectName("punkt")
        self.verticalLayout_5.addWidget(self.punkt)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_street = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_street.setFont(font)
        self.label_street.setAlignment(QtCore.Qt.AlignCenter)
        self.label_street.setObjectName("label_street")
        self.verticalLayout_6.addWidget(self.label_street)
        self.street = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.street.setFont(font)
        self.street.setObjectName("street")
        self.verticalLayout_6.addWidget(self.street)
        self.label_house = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_house.setFont(font)
        self.label_house.setAlignment(QtCore.Qt.AlignCenter)
        self.label_house.setObjectName("label_house")
        self.verticalLayout_6.addWidget(self.label_house)
        self.house = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.house.setFont(font)
        self.house.setObjectName("house")
        self.verticalLayout_6.addWidget(self.house)
        self.label_state = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_state.setFont(font)
        self.label_state.setAlignment(QtCore.Qt.AlignCenter)
        self.label_state.setObjectName("label_state")
        self.verticalLayout_6.addWidget(self.label_state)
        self.state = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.state.setFont(font)
        self.state.setObjectName("state")
        self.verticalLayout_6.addWidget(self.state)
        self.label_inn = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_inn.setFont(font)
        self.label_inn.setAlignment(QtCore.Qt.AlignCenter)
        self.label_inn.setObjectName("label_inn")
        self.verticalLayout_6.addWidget(self.label_inn)
        self.inn = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.inn.setFont(font)
        self.inn.setObjectName("inn")
        self.verticalLayout_6.addWidget(self.inn)
        self.label_snils = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_snils.setFont(font)
        self.label_snils.setAlignment(QtCore.Qt.AlignCenter)
        self.label_snils.setObjectName("label_snils")
        self.verticalLayout_6.addWidget(self.label_snils)
        self.snils = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.snils.setFont(font)
        self.snils.setObjectName("snils")
        self.verticalLayout_6.addWidget(self.snils)
        self.horizontalLayout.addLayout(self.verticalLayout_6)
        self.verticalLayout_7.addLayout(self.horizontalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.button_add = QtWidgets.QPushButton(self.centralwidget)
        self.button_add.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.button_add.setFont(font)
        self.button_add.setObjectName("button_add")
        self.verticalLayout_3.addWidget(self.button_add)
        self.button_load = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.button_load.setFont(font)
        self.button_load.setObjectName("button_load")
        self.verticalLayout_3.addWidget(self.button_load)
        self.verticalLayout_7.addLayout(self.verticalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.table_info = QtWidgets.QTableWidget(self.centralwidget)
        self.table_info.setObjectName("table_info")
        self.table_info.setColumnCount(20)
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
        item = QtWidgets.QTableWidgetItem()
        self.table_info.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_info.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_info.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_info.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_info.setHorizontalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_info.setHorizontalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_info.setHorizontalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_info.setHorizontalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_info.setHorizontalHeaderItem(19, item)
        self.verticalLayout.addWidget(self.table_info)
        self.verticalLayout_7.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Главное окно"))
        self.label_name.setText(_translate("MainWindow", "Имя"))
        self.label_surname.setText(_translate("MainWindow", "Фамилия"))
        self.label_patronymic.setText(_translate("MainWindow", "Отчество"))
        self.label_series.setText(_translate("MainWindow", "Серия"))
        self.label_number.setText(_translate("MainWindow", "Номер"))
        self.label_gender.setText(_translate("MainWindow", "Пол"))
        self.label_birth_date.setText(_translate("MainWindow", "Дата рождения"))
        self.label_birth_place.setText(_translate("MainWindow", "Место рождения"))
        self.label_issue_place.setText(_translate("MainWindow", "Кем выдан"))
        self.label_issue_date.setText(_translate("MainWindow", "Дата выдачи"))
        self.label_code.setText(_translate("MainWindow", "Код подразделения"))
        self.label_reg_date.setText(_translate("MainWindow", "Дата регистрации"))
        self.label_region.setText(_translate("MainWindow", "Регион"))
        self.label_ray.setText(_translate("MainWindow", "Район"))
        self.label_punkt.setText(_translate("MainWindow", "Пункт"))
        self.label_street.setText(_translate("MainWindow", "Улица"))
        self.label_house.setText(_translate("MainWindow", "Дом"))
        self.label_state.setText(_translate("MainWindow", "Отделение"))
        self.label_inn.setText(_translate("MainWindow", "ИНН"))
        self.label_snils.setText(_translate("MainWindow", "СНИЛС"))
        self.button_add.setText(_translate("MainWindow", "Добавить"))
        self.button_load.setText(_translate("MainWindow", "Добавить по фото"))
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
        item = self.table_info.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "Дата регистрации"))
        item = self.table_info.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "Регион"))
        item = self.table_info.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "Район"))
        item = self.table_info.horizontalHeaderItem(14)
        item.setText(_translate("MainWindow", "Пункт"))
        item = self.table_info.horizontalHeaderItem(15)
        item.setText(_translate("MainWindow", "Улица"))
        item = self.table_info.horizontalHeaderItem(16)
        item.setText(_translate("MainWindow", "Дом"))
        item = self.table_info.horizontalHeaderItem(17)
        item.setText(_translate("MainWindow", "Отделение"))
        item = self.table_info.horizontalHeaderItem(18)
        item.setText(_translate("MainWindow", "ИНН"))
        item = self.table_info.horizontalHeaderItem(19)
        item.setText(_translate("MainWindow", "СНИЛС"))
