# This is a sample Python script.

import sys
import time
from threading import Thread

from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt, QThreadPool, QRunnable

from PySide6.QtGui import QPalette, QColor
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLineEdit, QTableView
from visuPmk import Visu_ui
import pandas as pd
from multiprocessing import Process
from exchange import process_mb as p_mb

from exchange import myModbus, data_exchange
from queue import Queue



class Worker(QRunnable):
    '''
    Worker thread
    '''

    # @pyqtSlot()


class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            value = self._data.iloc[index.row(), index.column ()]
            return str(value)

    def rowCount(self, index):
        return self._data.shape[0]

    def columnCount(self, index):
        return self._data.shape[1]

    def headerData(self, section, orientation, role):
        # section is the index of the column/row.
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._data.columns[section])
            if orientation == Qt.Vertical:
                return str(self._data.index[section])
data = pd.DataFrame ( [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],

], columns=['Калал 1', 'Калал 2', 'Калал 3', 'Калал 4', 'Калал 5',
            'Калал 6', 'Калал 7', 'Калал 8', 'Калал 9', 'Калал 10'],
    index=['Режим работы:', 'Режим работы канала', 'Допустимые диапазоны:', 'Диапазон сопр. изоляции авар.',
           'Диапазон сопр. шлейфа авар.', 'Диапазон сопр. изоляции предупр.', 'Диапазон сопр. шлейфа предупр.',
           'Уставки:', 'Уставка напряжения на входе', 'Уставка сопр. изоляции 1', 'Уставка сопр. изоляции 2',
           'Уставка сопр. шлейфа', 'Текущие значения:', 'Сопр. изоляции 1', 'Сопр. изоляции 1',
           'Сопр. шлейфа', 'Напряжение на входе 1', 'Напряжение на входе 2',
           'Расчетное знач. объем. наряжение', 'Авария - "А", предупрежд. - "П"', 'Сопр. изоляции 1 ниже доп.',
           'Сопр. изоляции 2 ниже доп.', 'Сопр. шлейфа ниже доп.', 'Сопр. шлейфа выше доп.',
           'Напряжение на входе 1 выше доп.', 'Напряжение на входе 2 выше доп.'] )

class MainWindow(QtWidgets.QMainWindow, Visu_ui):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Visu_ui.__init__(self)
        self.setupUi(self)

        self.writeTabl()
        self.threadpool = QThreadPool ()
        print ( "Multithreading with maximum %d threads" % self.threadpool.maxThreadCount () )
        # self.table = self.tableView()
        # self.tableView_Arhive
        # self.tab_4
        self.tableView_Arhive
        # data = pd.DataFrame ( [
        #     [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        #     [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        #     [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        #     [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        #     [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        #     [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        #     [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        #     [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        #     [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        #     [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        #     [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        #     [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        #     [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        #     [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        #     [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        #     [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        #     [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        #     [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        #     [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        #     [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        #     [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        #     [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        #     [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        #     [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        #     [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        #     [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        #
        # ], columns=['Калал 1', 'Калал 2', 'Калал 3', 'Калал 4', 'Калал 5',
        #             'Калал 6', 'Калал 7', 'Калал 8', 'Калал 9', 'Калал 10'],
        #     index=['Режим работы:', 'Режим работы канала', 'Допустимые диапазоны:', 'Диапазон сопр. изоляции авар.',
        #            'Диапазон сопр. шлейфа авар.', 'Диапазон сопр. изоляции предупр.', 'Диапазон сопр. шлейфа предупр.',
        #            'Уставки:', 'Уставка напряжения на входе', 'Уставка сопр. изоляции 1', 'Уставка сопр. изоляции 2',
        #            'Уставка сопр. шлейфа', 'Текущие значения:', 'Сопр. изоляции 1', 'Сопр. изоляции 1',
        #            'Сопр. шлейфа', 'Напряжение на входе 1', 'Напряжение на входе 2',
        #            'Расчетное знач. объем. наряжение', 'Авария - "А", предупрежд. - "П"', 'Сопр. изоляции 1 ниже доп.',
        #            'Сопр. изоляции 2 ниже доп.', 'Сопр. шлейфа ниже доп.', 'Сопр. шлейфа выше доп.',
        #            'Напряжение на входе 1 выше доп.', 'Напряжение на входе 2 выше доп.'] )



        self.model = TableModel(data)
        self.tableView_Arhive.setModel(self.model)
        # self.setCentralWidget(self.tableView_Arhive)


        # self.ui.writeTabl()
        # self.ui.defAddMb()
        # self.show()
        # self.ui.add_rz1()


#

# visu = process_visu()

# endregion

# Press the green button in the gutter to run the script.


# if __name__ == '__main__':
#     app = QtWidgets.QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     # window.model.data([1][1], 1 )
#     app.exec()
#     class process_visu:
def appvisu():
    app = QtWidgets.QApplication ( sys.argv )
    window = MainWindow ()
    window.show ()
    # window.model.data([1][1], 1 )
    app.exec()

def exchang():
    m_m = myModbus()
    dat = data_exchange()
    while(True):
    # for i in range(1, 2):
        m_m.get_mode()
        res = dat.get_mode_device()
        print('выход блока =', res)

        if (dat.get_mode_device() != 0xF00F):

            m_m.con()

            res = dat.get_alarm_riz1()
            print('авария сопр. изляции 1 =', res)
            res = dat.get_delta_alarm()
            print('аварийный диапазон = ', res)
            res = dat.get_rz1()
            print('Сопротивление изоляции 1 = ', res)
        time.sleep(1)

    # appvisu()
    # th = Thread(target=exchang())
    # th2 = Thread(target=appvisu())

    # dp2 = p_mb(2,9600).exchang()

    # q = Queue()
    # th2 = Tread(target=p_mb.exchang, args=(), daemon=True)
    # th2.start()
    #



if __name__ == '__main__':
    q = Queue()

    th1 = Process(target=appvisu, args=(), daemon=True)
    th1.start()


    th2 = Process(target=exchang, args=(), daemon=True)
    th2.start()



    th1.join()
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
# def print_hi(name):
#
#     # Use a breakpoint in the code line below to debug your script.
#     # endregion
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


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

# class process_visu:
#     def appvisu(self):
#         app = QtWidgets.QApplication ( sys.argv )
#         window = MainWindow()
#         window.show()
#         # window.model.data([1][1], 1 )
#         app.exec()
#         window.ui.add_rz1([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

        # window.show()
        # # for i in range(1,10000):
        # #     window.ui.chn_mode([i, 12, 13, 14, 15, 16, 71, 81, 91, 101] )
        #
        # sys.exit(app.exec())