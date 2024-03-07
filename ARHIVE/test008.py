# -*- coding: utf-8 -*-

import time

import requests

from PySide6.QtCore import (QThread, Signal, Slot, QSize)
from PySide6.QtWidgets import (QApplication, QPushButton, QLabel, QVBoxLayout, QWidget)


class MyThread(QThread):
    signal_tuple = Signal(tuple)

    def __init__(self, func, *args, **kwargs):
        super().__init__()
        self. func = func
        self.args = args
        self.count: int = kwargs.get('count')

    def run(self):
        for idx in range(1, self.count + 1):
            result = self. func(*self. args)
            time. sleep(1)
            # Signal when task completes
            self. signal_tuple. emit((idx, result))


class MainWindow(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self. setup_ui()
        #
        self.button.clicked.connect(self.setup_thread)

    def setup_ui(self):
        self.setWindowTitle('demo')
        self. resize(QSize(250, 180))
        # create a vertical layout
        layout = QVBoxLayout()
        # Create a label
        self.label = QLabel('This is a label => ')
        layout. addWidget(self. label)
        # create a button
        self.button = QPushButton('Send Request')
        layout. addWidget(self. button)
        # Set the layout to the layout of the main window
        self. setLayout(layout)
        # show window
        self. show()

    def setup_thread(self):
        self.thread_ = MyThread(self.send_request,
                                count=10)
        self.thread_.signal_tuple.connect(self.thread_finished)
        self. thread_. start()

    def send_request(self):
        return requests.get('https://www.csdn.net/').text[:15]

    @Slot(tuple)
    def thread_finished(self, item):
        self.label.setText('This is a label => ' + str(item))


# if __name__ == '__main__':
app = QApplication([])
window = MainWindow()
window. show()
app.exec()