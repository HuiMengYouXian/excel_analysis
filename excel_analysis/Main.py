import sys

from PyQt5 import QtWidgets
from main_view import Ui_MainWindow


def show_main_window():
        app = QtWidgets.QApplication(sys.argv)
        mainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(mainWindow)
        mainWindow.show()
        sys.exit(app.exec_())


if __name__ == '__main__':
    show_main_window()