# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wish_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WishDialog(object):
    def setupUi(self, WishDialog):
        WishDialog.setObjectName("WishDialog")
        WishDialog.resize(317, 184)
        self.verticalLayout = QtWidgets.QVBoxLayout(WishDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.name_line = QtWidgets.QLineEdit(WishDialog)
        self.name_line.setObjectName("name_line")
        self.verticalLayout.addWidget(self.name_line)
        self.price_line = QtWidgets.QLineEdit(WishDialog)
        self.price_line.setObjectName("price_line")
        self.verticalLayout.addWidget(self.price_line)
        self.link_line = QtWidgets.QLineEdit(WishDialog)
        self.link_line.setText("")
        self.link_line.setObjectName("link_line")
        self.verticalLayout.addWidget(self.link_line)
        self.comment_line = QtWidgets.QLineEdit(WishDialog)
        self.comment_line.setObjectName("comment_line")
        self.verticalLayout.addWidget(self.comment_line)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.accept_wish = QtWidgets.QPushButton(WishDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.accept_wish.sizePolicy().hasHeightForWidth())
        self.accept_wish.setSizePolicy(sizePolicy)
        self.accept_wish.setObjectName("accept_wish")
        self.horizontalLayout.addWidget(self.accept_wish)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(WishDialog)
        QtCore.QMetaObject.connectSlotsByName(WishDialog)

    def retranslateUi(self, WishDialog):
        _translate = QtCore.QCoreApplication.translate
        WishDialog.setWindowTitle(_translate("WishDialog", "Add wish"))
        self.name_line.setPlaceholderText(_translate("WishDialog", "Название*"))
        self.price_line.setPlaceholderText(_translate("WishDialog", "Цена*"))
        self.link_line.setPlaceholderText(_translate("WishDialog", "Ссылка*"))
        self.comment_line.setPlaceholderText(_translate("WishDialog", "Примечание"))
        self.accept_wish.setText(_translate("WishDialog", "Add wish"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WishDialog = QtWidgets.QDialog()
    ui = Ui_WishDialog()
    ui.setupUi(WishDialog)
    WishDialog.show()
    sys.exit(app.exec_())
