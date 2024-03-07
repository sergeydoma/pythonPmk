# This is a sample Python script.

import sys
import time

from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt

from PySide6.QtGui import QPalette, QColor
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLineEdit, QTableView
from visuPmk import Visu_ui
import pandas as pd
from edit_dialog import Ui_MainWindow


class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self._data[0])



class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # self.writeTabl()
        # self.table = self.tableView()
        # self.tableView_Arhive
        # self.tab_4

        self.tableView_Arhive

        data = [
            [4, 9, 2],
            [1, 0, 0],
            [3, 5, 0],
            [3, 3, 2],
            [7, 8, 9],
        ]

        self.model = TableModel(data)
        self.tableView_Arhive.setModel(self.model)
        # self.setCentralWidget(self.tableView_Arhive)





#

# visu = process_visu()

# endregion

# Press the green button in the gutter to run the script.


# if __name__ == '__main__':
app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

