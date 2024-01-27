# This is a sample Python script.
import time

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import exchange


import os
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
# from exchange import myModbus
from ui_pmk20_001 import Ui_MainWindow
from threading import Thread
from exchange import exchang


# th =Thread(target=exchang() )

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)

def appvisu():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    time.sleep(1)
    th2 = Thread(target=appvisu())
    sys.exit(app.exec())

# Press the green button in the gutter to run the script.



if __name__ == '__main__':

    print_hi('PyCharm')

    # appvisu()
    th = Thread(target=exchang())
    # th2 = Thread(target=appvisu())



    th.start()

    th2.start()



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
