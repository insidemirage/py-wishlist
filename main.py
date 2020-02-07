# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtWidgets
import design

class Wish_App(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Wish_App()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()