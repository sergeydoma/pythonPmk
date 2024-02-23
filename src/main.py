# This is a sample Python script.

import sys
import time

from PySide6 import QtCore, QtGui, QtWidgets, uic
from PySide6.QtCore import Qt
from PySide6.QtGui import QPalette, QColor
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLineEdit
from multiprocessing import Process
from queue import Queue
from exchange import process_mb as p_mb

from exchange import data_exchange

from src.visuPmk import visu_ui

white = 'QPushButton{font-size: 24pt; font-weight: bold; color: #000000; background-color: #FFFFFF}'
yellow = 'QPushButton{font-size: 24pt; font-weight: bold; color: #3E0BC1; background-color: #E8FC03}'        #;  border: #000000
green = 'QPushButton{font-size: 24pt; font-weight: bold; color: #19305D; background-color: #35A941}'
root = 'QPushButton{font-size: 24pt; font-weight: bold; color: #FFFFFF; background-color: #FF0000}'            ##E6643D

setColor = [white, white, white,white,white,white,white,white,white,white,white,white,white,white,white,
            white,white,white,white,white]

setColor[0] = yellow
setColor[1] = green
setColor[2] = root

datE = data_exchange()

class TodoModel(QtCore.QAbstractListModel):
    def __init__(self, *args, todos=None, **kwargs):
        super(TodoModel, self).__init__(*args, **kwargs)
        self.todos = todos or []

    def data(self, index, role):
        if role == Qt.DisplayRole:
            # See below for the data structure.
            status, text = self.todos[index.row()]
            # Return the todo text only.
            return text

    def rowCount(self, index):
        return len(self.todos)

todos = [(False, 'an item'), (False, 'another item')]
model = TodoModel(todos)






# region classes
qt_creator_file = "mainwindow.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qt_creator_file)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui = visu_ui()
        self.ui.setupUi(self)
        self.ui.writeTabl()
        self.ui.defAddMb()
        self.show()
        # self.ui.add_rz1()


class process_visu:
    def appvisu(self):
        app = QApplication(sys.argv)

        window = MainWindow()
        window.ui.add_rz1([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

        window.show()
        # for i in range(1,10000):
        #     window.ui.chn_mode([i, 12, 13, 14, 15, 16, 71, 81, 91, 101] )

        sys.exit(app.exec())


# visu = process_visu()

# endregion

# Press the green button in the gutter to run the script.


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = MainWindow()

    sys.exit(app.exec())



    # appvisu()
    # th = Thread(target=exchang())
    # th2 = Thread(target=appvisu())

    # dp2 = p_mb(2,9600).exchang()

    # q = Queue()
    # th2 = Process(target=p_mb.exchang, args=(), daemon=True)
    # th2.start()
    #
    # th1 = Process(target=visu.appvisu(), args=(), daemon=True)
    # th1.start()
    #
    # th1.join()
    # th2.join()



    # p2.start()

    # # p1.start()
    # p2.join()
    # p1.join()

    # while True:
    #     # ex()
    #     pass

# appvisu()
# proc = Process(target=ex())
# proc.start()
def print_hi(name):

    # Use a breakpoint in the code line below to debug your script.
    # endregion
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


class lay:
    def __init__ (self, delta_alarm, delta_warning, name):
        self.delta_alarm = delta_alarm
        self.delta_warning = delta_warning
        self.name = name

    def layout(self):
        self.lineEdit_1 = QLineEdit('Диапазон Rz1 =')

# th.start()


# m_m.connect()

# th = Thread(target=func)
#
#
# th.start()
# Mod = myModbus()
# client = m_m.connect()
# try:
#     # Mod.con(1,9600)
#     client = Mod.con(1,9600)
#     res = client.read_holding_registers(0, count=10, unit=0x02).registers
#     # res2 = client.read_holding_registers(10, count=10, unit=0x02).registers


class Color(QWidget):
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

