import sys
from PyQt5.QtWidgets import *
from view import MainWindow
from PyQt5 import QtWidgets
from db import DB


def main():
    app = QtWidgets.QApplication(sys.argv)
    db = DB()
    window = MainWindow(db)
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()