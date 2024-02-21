# This is a sample Python script.

import sys

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



# region classes
class Color(QWidget):
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = visu_ui()
        self.ui.setupUi(self)
        self.ui.writeTabl()

        


class process_visu:
    def appvisu(self):

        app = QApplication(sys.argv)

        window = MainWindow()
        window.show()
        sys.exit(app.exec())


visu = process_visu()

# endregion

# Press the green button in the gutter to run the script.


if __name__ == '__main__':

    print_hi('PyCharm')

    # appvisu()
    # th = Thread(target=exchang())
    # th2 = Thread(target=appvisu())

    # dp2 = p_mb(2,9600).exchang()


    # temp = p_mb.exchang()
    q = Queue()
    th2 = Process(target=p_mb.exchang, args=(), daemon=True)
    th2.start()

    th1 = Process(target=visu.appvisu(), args=(), daemon=True)
    th1.start()

    th1.join()
    th2.join()



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
#     res3 = Mod.get_delta_Alarm()
#     print("Delta Alarm = ", res3)
#     # print(res2)
#     err = 0
#
# except Exception as e:
# # except ConnectionError:
#     print("Error33! " + str(e)+"FFFF!")
#     dd = e
#     print ('Number', e)
#     # print ('Con Error')
#     err = 1

# try:
#     res = client.read_holding_registers(0, count=10, unit=0x02).registers
#     res2 = client.read_holding_registers(10, count=10, unit=0x02).registers
#     print(res)
#     print(res2)
#     err = 0
#     client.close()
# except Exception as e:
#     print("Error Modbus! " + str(e))
#     dd = e
#     print("по порядку", dd)
#     err = 11

# except Exception as e:
# except ConnectionError:
#     print("Error! ")

# res = client.read_holding_registers(1, count=10, unit=0x02).registers
#
# print(res)
# print (err)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
