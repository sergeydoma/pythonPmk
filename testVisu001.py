import sys

from PySide6.QtGui import QPalette, QColor
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QGridLayout, \
    QHBoxLayout, QLineEdit, QFrame
from ui_pmk20_001 import Ui_MainWindow
from multiprocessing import Process
# from exchange import exchang as ex
from PySide6.QtCore import QRunnable, Slot, QThreadPool

white = 'QPushButton{font-size: 24pt; font-weight: bold; color: #000000; background-color: #FFFFFF}'
yellow = 'QPushButton{font-size: 24pt; font-weight: bold; color: #3E0BC1; background-color: #E8FC03}'  # ;  border: #000000
green = 'QPushButton{font-size: 24pt; font-weight: bold; color: #19305D; background-color: #35A941}'
root = 'QPushButton{font-size: 24pt; font-weight: bold; color: #FFFFFF; background-color: #FF0000}'  ##E6643D

setColor = [white, white, white, white, white, white, white, white, white, white, white, white, white, white, white,
            white, white, white, white, white]

setColor[0] = yellow
setColor[1] = green
setColor[2] = root


class lay:
    def __init__(self, delta_alarm, delta_warning, name):
        self.lineEdit_1 = QLineEdit("1-1")
        self.lineEdit_2 = QLineEdit("1-2")
        self.lineEdit_3 = QLineEdit("1-3")
        self.button_1 = QPushButton('Push')
        self.frame_1 = QFrame()

    def layout(self):
        layout1 = QVBoxLayout()
        self.lineEdit_1 = QLineEdit('Диапазон Rz1 =')
        out = layout1.addWidget(self.lineEdit_1)
        return out


# noinspection PyUnresolvedReferences
class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.lineEdit_1 = QLineEdit("1-1")
        self.lineEdit_2 = QLineEdit("1-2")
        self.lineEdit_3 = QLineEdit("1-3")
        self.button_1 = QPushButton('Push')
        self.frame_1 = QFrame()

        layout_1 = QVBoxLayout()

        layout_1.addWidget(self.lineEdit_1)
        layout_1.addWidget(self.lineEdit_2)
        layout_1.addWidget(self.lineEdit_3)
        layout_1.addWidget(self.button_1)
        layout_1.addWidget(self.frame_1)
        # self.setCentralWidget(lineEdit_1)

        # self.setWindowTitle('PMK-20')
        # # lay1 = lay(12, 22, '1-1')
        # # layout1 = lay1.layout()
        # layout1 = QVBoxLayout()
        # self.lineEdit_1 = QLineEdit('1-1')
        # self.lineEdit_2 = QLineEdit('1-2')
        # self.lineEdit_3 = QLineEdit('1-2')
        # layout1.addWidget(self.lineEdit_1)
        # layout1.addWidget(self.lineEdit_2)
        # layout1.addWidget(self.lineEdit_2)
        #
        #
        widget = QWidget()
        widget.setLayout(layout_1)
        self.setCentralWidget(widget)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
