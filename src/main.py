# This is a sample Python script.

import sys

from PySide6.QtGui import QPalette, QColor
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QGridLayout, \
    QHBoxLayout
from ui_pmk20_001 import Ui_MainWindow
from multiprocessing import Process
from exchange import exchang as ex
from PySide6.QtCore import QRunnable, Slot, QThreadPool
white = 'QPushButton{font-size: 24pt; font-weight: bold; color: #000000; background-color: #FFFFFF}'
yellow = 'QPushButton{font-size: 24pt; font-weight: bold; color: #3E0BC1; background-color: #E8FC03}'        #;  border: #000000
green = 'QPushButton{font-size: 24pt; font-weight: bold; color: #19305D; background-color: #35A941}'
root = 'QPushButton{font-size: 24pt; font-weight: bold; color: #FFFFFF; background-color: #FF0000}'            ##E6643D

setColor = [white, white, white,white,white,white,white,white,white,white,white,white,white,white,white,
            white,white,white,white,white]

setColor[0] = yellow
setColor[1] = green
setColor[2] = root
def print_hi(name):

    # Use a breakpoint in the code line below to debug your script.
    # endregion
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

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
        super(MainWindow, self).__init__()

        self.setWindowTitle('PMK-20')
        self.pushButton_0 = QPushButton('1-1')
        self.pushButton_0.setStyleSheet(setColor[0])
        # self.pushButton_1.setAlignment()
        self.pushButton_1 = QPushButton('1-2')
        self.pushButton_1.setStyleSheet(setColor[1])
        self.pushButton_2 = QPushButton('1-3')
        self.pushButton_2.setStyleSheet(setColor[2])
        self.pushButton_3 = QPushButton('1-4')
        self.pushButton_3.setStyleSheet(setColor[3])
        self.pushButton_4 = QPushButton('1-5')
        self.pushButton_4.setStyleSheet(setColor[4])
        self.pushButton_5 = QPushButton('1-6')
        self.pushButton_5.setStyleSheet(setColor[5])
        self.pushButton_6 = QPushButton('1-7')
        self.pushButton_6.setStyleSheet(setColor[6])
        self.pushButton_7 = QPushButton('1-8')
        self.pushButton_7.setStyleSheet(setColor[7])
        self.pushButton_8 = QPushButton('1-9')
        self.pushButton_8.setStyleSheet(setColor[8])
        self.pushButton_9 = QPushButton('1-10')
        self.pushButton_9.setStyleSheet(setColor[9])
        self.pushButton_10 = QPushButton('2-1')
        self.pushButton_10.setStyleSheet(setColor[10])
        self.pushButton_11 = QPushButton('2-2')
        self.pushButton_11.setStyleSheet(setColor[11])
        self.pushButton_12 = QPushButton('2-3')
        self.pushButton_12.setStyleSheet(setColor[12])
        self.pushButton_13 = QPushButton('2-4')
        self.pushButton_13.setStyleSheet(setColor[13])
        self.pushButton_14 = QPushButton('2-5')
        self.pushButton_14.setStyleSheet(setColor[14])
        self.pushButton_15 = QPushButton('2-6')
        self.pushButton_15.setStyleSheet(setColor[15])
        self.pushButton_16 = QPushButton('2-7')
        self.pushButton_16.setStyleSheet(setColor[16])
        self.pushButton_17 = QPushButton('2-8')
        self.pushButton_17.setStyleSheet(setColor[17])
        self.pushButton_18 = QPushButton('2-9')
        self.pushButton_18.setStyleSheet(setColor[18])
        self.pushButton_19 = QPushButton('2-10')
        self.pushButton_19.setStyleSheet(setColor[19])

        layout1 = QGridLayout()  #QVBoxLayout()
        layout2 = QHBoxLayout()
        layout3 = QHBoxLayout()

        # layout2.addWidget(Color('yellow'))

        layout1.addLayout(layout2, 1, 1)
        layout1.addLayout(layout3, 2,1)

        layout2.addWidget(self.pushButton_0)
        layout2.addWidget(self.pushButton_1)
        layout2.addWidget(self.pushButton_2)
        layout2.addWidget(self.pushButton_3)
        layout2.addWidget(self.pushButton_4)
        layout2.addWidget(self.pushButton_5)
        layout2.addWidget(self.pushButton_6)
        layout2.addWidget(self.pushButton_7)
        layout2.addWidget(self.pushButton_8)
        layout2.addWidget(self.pushButton_9)

        layout3.addWidget(self.pushButton_10)
        layout3.addWidget(self.pushButton_11)
        layout3.addWidget(self.pushButton_12)
        layout3.addWidget(self.pushButton_13)
        layout3.addWidget(self.pushButton_14)
        layout3.addWidget(self.pushButton_15)
        layout3.addWidget(self.pushButton_16)
        layout3.addWidget(self.pushButton_17)
        layout3.addWidget(self.pushButton_18)
        layout3.addWidget(self.pushButton_19)

        layout1.setSpacing(1)
        # layout.addWidget(self.label1, 0, 0)
        # layout.addWidget(Color('yellow'), 0, 1)
        # layout.addWidget(self.label2, 0, 1)
        # layout.addWidget(self.label5, 0, 2)
        # layout.addWidget(self.label3, 0, 8)
        # layout.addWidget(self.label4, 3, 1)
        #
        # layout.setContentsMargins(0, 0, 0, 0)
        # layout.setSpacing(5)

        widget = QWidget()
        widget.setLayout(layout1)
        self.setCentralWidget(widget)


def appvisu():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    # time.sleep(1)
    # th2 = Thread(target=appvisu())
    # proc = Process(target=ex())
    # proc.start()
    # proc.join()

    sys.exit(app.exec())

# endregion

# Press the green button in the gutter to run the script.


if __name__ == '__main__':

    print_hi('PyCharm')

    # appvisu()
    # th = Thread(target=exchang())
    # th2 = Thread(target=appvisu())

    p2 = Process(target=ex, daemon=True)

    p2.start()

    p1 = Process(target=appvisu(), daemon=True)

    p1.start()
    # p1.start()
    p2.join()
    p1.join()

    while True:
        # ex()
        pass

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
