import sys

from PySide6.QtWidgets import QApplication, QMainWindow

from dialog import Ui_Dialog


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_Dialog()
        # self.ui.setupUi(self)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
    




# exchange
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# проверка