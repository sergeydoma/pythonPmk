import binascii

from PySide6 import QtGui
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QTableWidgetItem

from src.edit_dialog import Ui_MainWindow
from exchange import dat
from exchange import mMod

class visu_ui(Ui_MainWindow):
    
    

    
    def writeTabl(self):
            # tblitems.setItem(2,2, "Ура!")

            self.lineEdit_1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter) # начальная надпись
            addMb = self.lineEdit_1.text()
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

            self.lineEdit_1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)


            # self.Button_con.clicked.connect(defAddMb)

    # def one_click(self):
    def defAddMb(self):

        self.lineEdit_1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
        addMb = self.lineEdit_1.text()
        # h_addMb = int(addMb)
        # h_addMb = addMb.encode('hex')
        # h_addMb = addMb.encode("utf-8").hex()

        try:

            int_addMb = int(addMb,16)

            h_addMb = hex(int_addMb)

            dat.set_id_serial(h_addMb)

            print(dat.get_id_serial())

        except:
            mess1 = "Ошибка формата ввода номера устройства\n на шине Modbus RTU!"
            dat.set_message(mess1)
            self.label_info.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
            self.label_info.setText(dat.get_message())

        else:
            mMod.con


   
    # def readTabl(selfs):
        # self.Button_con.c
    
            
    