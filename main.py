# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtWidgets, QtCore
import design
import pymysql
import config
import random
import string


class DBWriter:
    def __init__(self, host:str, user:str, password:str, database:str, table:str = "wish_list"):
        self._host = host
        self._user = user
        self._password = password
        self._database = database
        self._table = table

    def _connect(self):
        return pymysql.connect(self._host, self._user, self._password, self._database)

    @staticmethod
    def _rand_id():
        return "".join([random.choice(string.ascii_lowercase) for s in range(10)])

    # Returns all data
    def get_info(self):
        connection = self._connect()
        with connection:
            curs = connection.cursor()
            curs.execute(f"SELECT * FROM {self._table}")
            rows = curs.fetchall()
            result = []
            for row in rows:
                result.append(row)
            return result

    # Insert element into base
    def add_item(self, data):
        connection = self._connect()
        with connection:
            curs = connection.cursor()
            bdw = [self._table, self._rand_id()]
            bdw.extend(data)
            curs.execute("INSERT INTO wish_list VALUES('{}','{}','{}','{}', '{}')".format(self._rand_id(),
                                                                                          data["name"], data["price"],
                                                                                          data["link"], data["comment"]))

    # Update element information
    def change_item(self, data):
        connection = self._connect()
        with connection:
            curs = connection.cursor()
            curs.execute("UPDATE wish_list SET Name='{}', Price='{}', Link='{}',Comment='{}' WHERE Id='{}'".format(data["name"],
                                                                                                                  data["price"],
                                                                                                                  data["link"],
                                                                                                                  data["comment"],
                                                                                                                 data["id"]))

    # Removes element
    def remove_item(self, id):
        connection = self._connect()
        with connection:
            curs = connection.cursor()
            curs.execute(f"DELETE FROM wish_list WHERE Id='{id}'")


class WishDialog(QtWidgets.QDialog, design.Ui_WishDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.accept_wish.clicked.connect(self._check_inputs)

    def _check_inputs(self):
        if self.name_line.text() != "" and self.price_line.text() != "" and self.link_line.text() != "":
            self.accept()
        else:
            error_dialog = QtWidgets.QMessageBox()
            error_dialog.setIcon(QtWidgets.QMessageBox.Critical)
            error_dialog.setText("Ошибка")
            error_dialog.setInformativeText("Заполните все поля со *")
            error_dialog.setWindowTitle("Error")
            error_dialog.exec_()

    def get_rows(self):
        name = self.name_line.text()
        price = self.price_line.text()
        link = self.link_line.text()
        comment = self.comment_line.text()
        return {"name": name, "price": price, "link": link, "comment": comment}


class WishAddDialog(WishDialog):
    def __init__(self, parent = None):
        super().__init__(parent)


class WishChangeDialog(WishDialog):
    def __init__(self, data, parent = None):
        super().__init__(parent)
        self.link_line.setText(data["link"])
        self.price_line.setText(data["price"])
        self.name_line.setText(data["name"])
        self.comment_line.setText(data["comment"])


class WishApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.add_wish.clicked.connect(self._show_add_dialog)
        self.db_writer = DBWriter(config.host, config.user, config.password, config.database)
        self._update()
        self.table_widjet.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.table_widjet.customContextMenuRequested.connect(self.context)

    def _show_edit_dialog(self, point):
        item = self.table_widjet.itemAt(point).row()
        data = {
            "name": self._list[item][1],
            "price": self._list[item][2],
            "link": self._list[item][3],
            "comment": self._list[item][4],
        }
        dialog = WishChangeDialog(data)
        if dialog.exec_():
            result = dialog.get_rows()
            data = {
                "name": result["name"],
                "price": result["price"],
                "link": result["link"],
                "comment": result["comment"],
                "id": self._list[item][0]
            }
            self.db_writer.change_item(data)
            self._update()

    # Table context menu
    def context(self, point):
        menu = QtWidgets.QMenu()
        if self.table_widjet.itemAt(point):
            edit_item = QtWidgets.QAction('Редактировать', menu)
            edit_item.triggered.connect(lambda p: self._show_edit_dialog(point))
            remove_item = QtWidgets.QAction("Удалить", menu)
            remove_item.triggered.connect(lambda p: self.remove_item(point))
            menu.addAction(edit_item)
            menu.addAction(remove_item)
        else:
            pass
        menu.exec(self.table_widjet.mapToGlobal(point))

    def remove_item(self, point):
        item = self.table_widjet.itemAt(point).row()
        self.db_writer.remove_item(self._list[item][0])
        self._update()

    def _show_add_dialog(self):
        dialog = WishAddDialog()
        if dialog.exec_():
            result = dialog.get_rows()
            self.db_writer.add_item(result)
            self._list = self._update()

    # Updates information
    def _update(self):
        rows = self.db_writer.get_info()
        self._list = rows
        self.table_widjet.setRowCount(0)
        for row_number, row_data in enumerate(rows):
            self.table_widjet.insertRow(row_number)
            for column_number, column_data in enumerate(row_data[1:]):
                self.table_widjet.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(column_data)))

        return True


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = WishApp()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()