import sys
from PySide6.QtCore import QObject
from PySide6 import QtGui
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QTableWidgetItem, QPushButton,  QApplication, QMainWindow

from edit_dialog import Ui_MainWindow


class visu_ui(Ui_MainWindow):
    
    

    
    def writeTabl(self):
            # tblitems.setItem(2,2, "Ура!")
            self.tblitems_2.setItem(1, 1, QTableWidgetItem("Ура!!!!!", ))
            self.tblitems_1.setItem(22, 0, QTableWidgetItem("П"))
            self.tblitems_1.item(22, 0).setBackground(QtGui.QColor(255, 255, 0))  # желтый
            self.tblitems_1.item(22, 0).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
            self.tblitems_1.setItem(23, 0, QTableWidgetItem("А"))
            self.tblitems_1.item(23, 0).setBackground(QtGui.QColor(255, 0, 0))  # Красный
            # self.tblitems_1.item(23, 0).setTextColor(QtGui.QColor(255, 255, 255))  # белый
            self.tblitems_1.item(23, 0).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)

            self.Button_con.clicked.connect(self.defAddMb)
            
            # self.Button_con.clicked.connect(defAddMb)

    # def one_click(self):
    def defAddMb(self):

            print("Click connect!")
    

   
    # def readTabl(selfs):
        # self.Button_con.c
    
            
    