# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DeleteWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 192)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_series = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_series.setFont(font)
        self.label_series.setObjectName("label_series")
        self.verticalLayout.addWidget(self.label_series)
        self.series = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.series.setFont(font)
        self.series.setObjectName("series")
        self.verticalLayout.addWidget(self.series)
        self.label_number = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_number.setFont(font)
        self.label_number.setObjectName("label_number")
        self.verticalLayout.addWidget(self.label_number)
        self.number = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.number.setFont(font)
        self.number.setObjectName("number")
        self.verticalLayout.addWidget(self.number)
        self.button_delete = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.button_delete.setFont(font)
        self.button_delete.setObjectName("button_delete")
        self.verticalLayout.addWidget(self.button_delete)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Удалить"))
        self.label_series.setText(_translate("Dialog", "Серия"))
        self.label_number.setText(_translate("Dialog", "Номер"))
        self.button_delete.setText(_translate("Dialog", "Удалить"))
