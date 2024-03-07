import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QHBoxLayout
from PySide6.QtGui import QIcon, Qt


path_to_the_icon = os.path.join("../..", "icons", "../python.png")

app = QApplication(sys.argv)
main_window = QMainWindow()
main_window.show()


app.exec()
print("Application is closed!")
class Proba:

    __argum = 533

    def __init__(self, addr, rate):


        """
        __init__
        """
        self.addr = addr
        self.rate = rate


    def area(self):
        """
        area
        :return:
        """
        return self.__argum

    def current(self):
        """
        current
        :return:
        """
        self.__argum = 999

moca = Proba(2,1)
moca.current()

print (moca.area())

