# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SecondPageWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1663, 754)
        self.label_image = QtWidgets.QLabel(Dialog)
        self.label_image.setGeometry(QtCore.QRect(20, 20, 1001, 711))
        self.label_image.setObjectName("label_image")
        self.state = QtWidgets.QLineEdit(Dialog)
        self.state.setGeometry(QtCore.QRect(1360, 420, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.state.setFont(font)
        self.state.setText("")
        self.state.setObjectName("state")
        self.button_add = QtWidgets.QPushButton(Dialog)
        self.button_add.setGeometry(QtCore.QRect(1360, 470, 281, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.button_add.setFont(font)
        self.button_add.setObjectName("button_add")
        self.ray = QtWidgets.QLineEdit(Dialog)
        self.ray.setGeometry(QtCore.QRect(1050, 420, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ray.setFont(font)
        self.ray.setObjectName("ray")
        self.house = QtWidgets.QLineEdit(Dialog)
        self.house.setGeometry(QtCore.QRect(1360, 340, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.house.setFont(font)
        self.house.setObjectName("house")
        self.label_street = QtWidgets.QLabel(Dialog)
        self.label_street.setGeometry(QtCore.QRect(1360, 220, 161, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        self.label_street.setFont(font)
        self.label_street.setObjectName("label_street")
        self.region = QtWidgets.QLineEdit(Dialog)
        self.region.setGeometry(QtCore.QRect(1050, 340, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.region.setFont(font)
        self.region.setObjectName("region")
        self.label_state = QtWidgets.QLabel(Dialog)
        self.label_state.setGeometry(QtCore.QRect(1360, 380, 161, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        self.label_state.setFont(font)
        self.label_state.setObjectName("label_state")
        self.label_punkt = QtWidgets.QLabel(Dialog)
        self.label_punkt.setGeometry(QtCore.QRect(1050, 460, 121, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        self.label_punkt.setFont(font)
        self.label_punkt.setObjectName("label_punkt")
        self.punkt = QtWidgets.QLineEdit(Dialog)
        self.punkt.setGeometry(QtCore.QRect(1050, 500, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.punkt.setFont(font)
        self.punkt.setObjectName("punkt")
        self.label_reg_date = QtWidgets.QLabel(Dialog)
        self.label_reg_date.setGeometry(QtCore.QRect(1050, 220, 181, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        self.label_reg_date.setFont(font)
        self.label_reg_date.setObjectName("label_reg_date")
        self.label_region = QtWidgets.QLabel(Dialog)
        self.label_region.setGeometry(QtCore.QRect(1050, 300, 161, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        self.label_region.setFont(font)
        self.label_region.setObjectName("label_region")
        self.street = QtWidgets.QLineEdit(Dialog)
        self.street.setGeometry(QtCore.QRect(1360, 260, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.street.setFont(font)
        self.street.setObjectName("street")
        self.reg_date = QtWidgets.QLineEdit(Dialog)
        self.reg_date.setGeometry(QtCore.QRect(1050, 260, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.reg_date.setFont(font)
        self.reg_date.setObjectName("reg_date")
        self.label_house = QtWidgets.QLabel(Dialog)
        self.label_house.setGeometry(QtCore.QRect(1360, 300, 161, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        self.label_house.setFont(font)
        self.label_house.setObjectName("label_house")
        self.label_ray = QtWidgets.QLabel(Dialog)
        self.label_ray.setGeometry(QtCore.QRect(1050, 380, 151, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        self.label_ray.setFont(font)
        self.label_ray.setObjectName("label_ray")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Вторая страница"))
        self.label_image.setText(_translate("Dialog", "TextLabel"))
        self.button_add.setText(_translate("Dialog", "Далее"))
        self.label_street.setText(_translate("Dialog", "Улица"))
        self.label_state.setText(_translate("Dialog", "Отделение"))
        self.label_punkt.setText(_translate("Dialog", "Пункт"))
        self.label_reg_date.setText(_translate("Dialog", "Дата регистрации"))
        self.label_region.setText(_translate("Dialog", "Регион"))
        self.label_house.setText(_translate("Dialog", "Дом"))
        self.label_ray.setText(_translate("Dialog", "Район"))