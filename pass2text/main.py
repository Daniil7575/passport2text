import sys
# from Windows import Window, EditPersonWindow, WindowsManager
# from DataBase import DataBase
from PyQt5.QtWidgets import *
# from Docxcreating import Docxcreating
from view import MainWindow
from PyQt5 import QtWidgets
from db import DB


# def main():
#     app = QApplication(sys.argv)

#     data = DataBase.DataBaseCluster('SQLite/SQLiteBase.db')
#     windows_manager = WindowsManager.WindowsManager()
#     new_person_window = EditPersonWindow.EditPersonWindow(data, windows_manager)
#     main_window = Window.MainWindow(data, windows_manager)
#     windows = {
#         WindowsManager.WindowsNames.MainWindow: main_window,
#         WindowsManager.WindowsNames.EditPersonWindow: new_person_window
#     }
#     windows_manager.windows = windows
#     main_window.show()
#     app.exec()

def main():
    app = QtWidgets.QApplication(sys.argv)
    db = DB()
    window = MainWindow(db)
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()