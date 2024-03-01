import binascii

from PySide6 import QtGui
from PySide6.QtCore import Qt, QRunnable, QThreadPool
from PySide6.QtWidgets import QTableWidgetItem

from src.edit_dialog import Ui_MainWindow
from exchange import data_exchange
from exchange import mMod
# from main import wo
import time
from exchange import data_exchange


class Visu_ui(Ui_MainWindow, data_exchange):

    # self.dat = data_exchange()

    def __init__(self):
        Ui_MainWindow.__init__(self)
        data_exchange.__init__(self)
        self.dat = data_exchange()

    def writeTabl(self):
        self.tblitems_2.setItem(1, 1, QTableWidgetItem("Ура!!!!!", ))
        self.tblitems_1.setItem(22, 0, QTableWidgetItem("П"))
        self.tblitems_1.item(22, 0).setBackground(QtGui.QColor(255, 255, 0))  # желтый
        self.tblitems_1.item(22, 0).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
        self.tblitems_1.setItem(23, 0, QTableWidgetItem("А"))
        self.tblitems_1.item(23, 0).setBackground(QtGui.QColor(255, 0, 0))  # Красный
        # self.tblitems_1.item(23, 0).setTextColor(QtGui.QColor(255, 255, 255))  # белый
        self.tblitems_1.item(23, 0).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)

        self.Button_con.clicked.connect(self.defAddMb)

        self.label_info.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
        self.label_info.setText('Выберите номер устройства на шине Modbus RTU \n и нажмите кнопку "Подключить"')

        # self.lineEdit_1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
    def chn_mode(self, modeCH):
        for i in range(0, 10):
            self.tblitems_1.setItem(1, i, QTableWidgetItem(str(modeCH[i])))

    def add_rz1(self, rz1):
        for i in range(0, 10):
            self.tblitems_1.setItem(21, i, QTableWidgetItem(str(rz1[i])))

            # self.Button_con.clicked.connect(defAddMb)

        # def one_click(self):
    # @staticmethod
    def defAddMb(self):
        # self.lineEdit_1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)

        tCombo1 = int(self.comboBox_1.currentText(), 16)
        tCombo2 = int(self.comboBox_2.currentText(), 16)
        intCombo = tCombo1 * 16 + tCombo2
        self.dat.set_id_serial(intCombo)
        print('ВВеден номер = ',self.dat.get_id_serial())
        worker = Worker()
        self.threadpool.start(worker )
        # mMod.con

        # addMb = self.lineEdit_1.text()
        return intCombo

            # except:
            #     mess1 = "Ошибка формата вводимого номера устройства!\n(Допустимо - 00...FD)"
            #     dat.set_message(mess1)
            #     self.label_info.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
            #     self.label_info.setText(dat.get_message())
            #
            # else:
            #     mMod.con



            # def readTabl(selfs):
            # self.Button_con.c


class Worker ( QRunnable ):
    """
    Worker thread
    """


    # @pyqtSlot()
    def run(self):
        '''
        Your code goes in this function
        '''
        # while (1):
        #     print("Thread start")
        #     time.sleep ( 5 )
        #     print ("Thread complete")

