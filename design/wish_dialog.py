# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wish_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_add_wish_dialog(object):
    def setupUi(self, add_wish_dialog):
        add_wish_dialog.setObjectName("add_wish_dialog")
        add_wish_dialog.resize(317, 186)
        self.verticalLayout = QtWidgets.QVBoxLayout(add_wish_dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.name_line = QtWidgets.QLineEdit(add_wish_dialog)
        self.name_line.setObjectName("name_line")
        self.verticalLayout.addWidget(self.name_line)
        self.price_line = QtWidgets.QLineEdit(add_wish_dialog)
        self.price_line.setObjectName("price_line")
        self.verticalLayout.addWidget(self.price_line)
        self.link_line = QtWidgets.QLineEdit(add_wish_dialog)
        self.link_line.setText("")
        self.link_line.setObjectName("link_line")
        self.verticalLayout.addWidget(self.link_line)
        self.comment_line = QtWidgets.QLineEdit(add_wish_dialog)
        self.comment_line.setObjectName("comment_line")
        self.verticalLayout.addWidget(self.comment_line)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(add_wish_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(add_wish_dialog)
        QtCore.QMetaObject.connectSlotsByName(add_wish_dialog)

    def retranslateUi(self, add_wish_dialog):
        _translate = QtCore.QCoreApplication.translate
        add_wish_dialog.setWindowTitle(_translate("add_wish_dialog", "Add wish"))
        self.name_line.setPlaceholderText(_translate("add_wish_dialog", "Название*"))
        self.price_line.setPlaceholderText(_translate("add_wish_dialog", "Цена*"))
        self.link_line.setPlaceholderText(_translate("add_wish_dialog", "Ссылка*"))
        self.comment_line.setPlaceholderText(_translate("add_wish_dialog", "Примечание"))
        self.pushButton.setText(_translate("add_wish_dialog", "Add wish"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    add_wish_dialog = QtWidgets.QDialog()
    ui = Ui_add_wish_dialog()
    ui.setupUi(add_wish_dialog)
    add_wish_dialog.show()
    sys.exit(app.exec_())
