import minimalmodbus
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

import sys
import time
from multiprocessing import Process
from multiprocessing.sharedctypes import RawArray

import numpy as np
import pandas as pd

from PySide6 import QtCore, QtGui
from PySide6.QtCore import QAbstractTableModel, Qt, QTimer
from PySide6.QtWidgets import QTableView, QMainWindow, QApplication, QTableWidgetItem
from numpy import frombuffer
from numpy import double
from edit_dialog import Ui_MainWindow
# from myModbus import myModbus
import time


import psycopg2
from psycopg2 import Error

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pmk20_001.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHeaderView, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QStatusBar, QTabWidget, QTableView,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1549, 1000)
        MainWindow.setStyleSheet(u"background-color: rgb(189, 192, 144);\n"
"border-color: rgb(29, 30, 17);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        font = QFont()
        font.setFamilies([u"Sans Serif"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.tabWidget.setFont(font)
        self.tabWidget.setFocusPolicy(Qt.ClickFocus)
        self.tabWidget.setStyleSheet(u"font: 12pt \"Sans Serif\";\n"
"background-color: rgb(234, 232, 220);\n"
"color: rgb(0, 0, 0);")
        self.tabWidget.setDocumentMode(False)
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.tableWidget_PMK = QTableWidget(self.tab_1)
        if (self.tableWidget_PMK.columnCount() < 1):
            self.tableWidget_PMK.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_PMK.setHorizontalHeaderItem(0, __qtablewidgetitem)
        if (self.tableWidget_PMK.rowCount() < 6):
            self.tableWidget_PMK.setRowCount(6)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignJustify|Qt.AlignVCenter);
        self.tableWidget_PMK.setVerticalHeaderItem(0, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_PMK.setVerticalHeaderItem(1, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_PMK.setVerticalHeaderItem(2, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_PMK.setVerticalHeaderItem(3, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_PMK.setVerticalHeaderItem(4, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_PMK.setVerticalHeaderItem(5, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_PMK.setItem(0, 0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_PMK.setItem(1, 0, __qtablewidgetitem8)
        self.tableWidget_PMK.setObjectName(u"tableWidget_PMK")
        self.tableWidget_PMK.setGeometry(QRect(680, 50, 711, 211))
        font1 = QFont()
        font1.setFamilies([u"Sans Serif"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setKerning(True)
        font1.setHintingPreference(QFont.PreferFullHinting)
        self.tableWidget_PMK.setFont(font1)
        self.tableWidget_PMK.setStyleSheet(u"border-color: rgb(0, 85, 0);")
        self.tableWidget_PMK.setSortingEnabled(False)
        self.tableWidget_PMK.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_PMK.horizontalHeader().setDefaultSectionSize(470)
        self.tableWidget_PMK.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_PMK.verticalHeader().setStretchLastSection(True)
        self.label_info = QLabel(self.tab_1)
        self.label_info.setObjectName(u"label_info")
        self.label_info.setGeometry(QRect(50, 50, 431, 151))
        self.label_info.setStyleSheet(u"border-color: rgb(170, 170, 0);")
        self.label_info.setFrameShape(QFrame.Box)
        self.label_info.setFrameShadow(QFrame.Plain)
        self.label_info.setLineWidth(1)
        self.layoutWidget = QWidget(self.tab_1)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(50, 230, 371, 72))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.comboBox_1 = QComboBox(self.layoutWidget)
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.setObjectName(u"comboBox_1")

        self.gridLayout.addWidget(self.comboBox_1, 1, 0, 1, 1)

        self.Button_con = QPushButton(self.layoutWidget)
        self.Button_con.setObjectName(u"Button_con")
        self.Button_con.setStyleSheet(u"background-color: rgb(213, 213, 159);")

        self.gridLayout.addWidget(self.Button_con, 1, 2, 1, 1)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)

        self.comboBox_2 = QComboBox(self.layoutWidget)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout.addWidget(self.comboBox_2, 1, 1, 1, 1)

        self.tblitems_d = QTableWidget(self.tab_1)
        if (self.tblitems_d.columnCount() < 10):
            self.tblitems_d.setColumnCount(10)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tblitems_d.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tblitems_d.setHorizontalHeaderItem(1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tblitems_d.setHorizontalHeaderItem(2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tblitems_d.setHorizontalHeaderItem(3, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tblitems_d.setHorizontalHeaderItem(4, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tblitems_d.setHorizontalHeaderItem(5, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tblitems_d.setHorizontalHeaderItem(6, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tblitems_d.setHorizontalHeaderItem(7, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tblitems_d.setHorizontalHeaderItem(8, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tblitems_d.setHorizontalHeaderItem(9, __qtablewidgetitem18)
        if (self.tblitems_d.rowCount() < 8):
            self.tblitems_d.setRowCount(8)
        font2 = QFont()
        font2.setBold(True)
        font2.setItalic(True)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setFont(font2);
        self.tblitems_d.setVerticalHeaderItem(0, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tblitems_d.setVerticalHeaderItem(1, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tblitems_d.setVerticalHeaderItem(2, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tblitems_d.setVerticalHeaderItem(3, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setFont(font2);
        self.tblitems_d.setVerticalHeaderItem(4, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tblitems_d.setVerticalHeaderItem(5, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tblitems_d.setVerticalHeaderItem(6, __qtablewidgetitem25)
        icon = QIcon(QIcon.fromTheme(u"accessories-calculator"))
        __qtablewidgetitem26 = QTableWidgetItem()
        __qtablewidgetitem26.setText(u"\u041d\u0435\u0438\u0441\u043f\u0440\u0430\u0432\u043d\u043e\u0441\u0442\u044c \u0441\u043c\u0435\u0449\u0435\u043d\u0438\u044f -100 \u0412");
        __qtablewidgetitem26.setIcon(icon);
        self.tblitems_d.setVerticalHeaderItem(7, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        __qtablewidgetitem27.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled|Qt.ItemIsAutoTristate);
        self.tblitems_d.setItem(6, 0, __qtablewidgetitem27)
        self.tblitems_d.setObjectName(u"tblitems_d")
        self.tblitems_d.setGeometry(QRect(40, 440, 1401, 271))
        self.tblitems_d.setFont(font)
        self.tblitems_d.setLayoutDirection(Qt.LeftToRight)
        self.tblitems_d.setShowGrid(True)
        self.tblitems_d.setGridStyle(Qt.SolidLine)
        self.tblitems_d.setSortingEnabled(False)
        self.tblitems_d.setRowCount(8)
        self.tblitems_d.horizontalHeader().setVisible(True)
        self.tblitems_d.horizontalHeader().setCascadingSectionResizes(True)
        self.tblitems_d.horizontalHeader().setMinimumSectionSize(90)
        self.tblitems_d.horizontalHeader().setDefaultSectionSize(110)
        self.tblitems_d.horizontalHeader().setHighlightSections(True)
        self.tblitems_d.horizontalHeader().setProperty("showSortIndicator", True)
        self.tblitems_d.horizontalHeader().setStretchLastSection(True)
        self.tblitems_d.verticalHeader().setVisible(True)
        self.tblitems_d.verticalHeader().setCascadingSectionResizes(True)
        self.tblitems_d.verticalHeader().setHighlightSections(True)
        self.tblitems_d.verticalHeader().setProperty("showSortIndicator", False)
        self.tblitems_d.verticalHeader().setStretchLastSection(True)
        self.label_2 = QLabel(self.tab_1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setEnabled(False)
        self.label_2.setGeometry(QRect(50, 410, 181, 17))
        self.label_2.setFont(font)
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tblitems_1 = QTableWidget(self.tab_2)
        if (self.tblitems_1.columnCount() < 10):
            self.tblitems_1.setColumnCount(10)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tblitems_1.setHorizontalHeaderItem(0, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tblitems_1.setHorizontalHeaderItem(1, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tblitems_1.setHorizontalHeaderItem(2, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tblitems_1.setHorizontalHeaderItem(3, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tblitems_1.setHorizontalHeaderItem(4, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tblitems_1.setHorizontalHeaderItem(5, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tblitems_1.setHorizontalHeaderItem(6, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tblitems_1.setHorizontalHeaderItem(7, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tblitems_1.setHorizontalHeaderItem(8, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tblitems_1.setHorizontalHeaderItem(9, __qtablewidgetitem37)
        if (self.tblitems_1.rowCount() < 27):
            self.tblitems_1.setRowCount(27)
        __qtablewidgetitem38 = QTableWidgetItem()
        __qtablewidgetitem38.setFont(font2);
        self.tblitems_1.setVerticalHeaderItem(0, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tblitems_1.setVerticalHeaderItem(1, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        __qtablewidgetitem40.setFont(font2);
        self.tblitems_1.setVerticalHeaderItem(2, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tblitems_1.setVerticalHeaderItem(3, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.tblitems_1.setVerticalHeaderItem(4, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.tblitems_1.setVerticalHeaderItem(5, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.tblitems_1.setVerticalHeaderItem(6, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        __qtablewidgetitem45.setFont(font2);
        self.tblitems_1.setVerticalHeaderItem(7, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.tblitems_1.setVerticalHeaderItem(8, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.tblitems_1.setVerticalHeaderItem(9, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        __qtablewidgetitem48.setText(u"\u0423\u0441\u0442\u0430\u0432\u043a\u0430 \u0441\u043e\u043f\u0440. \u0438\u0437\u043e\u043b\u044f\u0446\u0438\u0438 2 (\u041c\u041e\u043c)");
        __qtablewidgetitem48.setIcon(icon);
        self.tblitems_1.setVerticalHeaderItem(10, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.tblitems_1.setVerticalHeaderItem(11, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        __qtablewidgetitem50.setFont(font2);
        self.tblitems_1.setVerticalHeaderItem(12, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.tblitems_1.setVerticalHeaderItem(13, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.tblitems_1.setVerticalHeaderItem(14, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.tblitems_1.setVerticalHeaderItem(15, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.tblitems_1.setVerticalHeaderItem(16, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        self.tblitems_1.setVerticalHeaderItem(17, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        self.tblitems_1.setVerticalHeaderItem(18, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        self.tblitems_1.setVerticalHeaderItem(19, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        __qtablewidgetitem58.setFont(font2);
        self.tblitems_1.setVerticalHeaderItem(20, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        self.tblitems_1.setVerticalHeaderItem(21, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        self.tblitems_1.setVerticalHeaderItem(22, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        self.tblitems_1.setVerticalHeaderItem(23, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        self.tblitems_1.setVerticalHeaderItem(24, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        self.tblitems_1.setVerticalHeaderItem(25, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        self.tblitems_1.setVerticalHeaderItem(26, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        __qtablewidgetitem65.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled|Qt.ItemIsAutoTristate);
        self.tblitems_1.setItem(9, 0, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        __qtablewidgetitem66.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(21, 0, __qtablewidgetitem66)
        __qtablewidgetitem67 = QTableWidgetItem()
        __qtablewidgetitem67.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(21, 1, __qtablewidgetitem67)
        __qtablewidgetitem68 = QTableWidgetItem()
        __qtablewidgetitem68.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(21, 2, __qtablewidgetitem68)
        __qtablewidgetitem69 = QTableWidgetItem()
        __qtablewidgetitem69.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(21, 3, __qtablewidgetitem69)
        __qtablewidgetitem70 = QTableWidgetItem()
        __qtablewidgetitem70.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(21, 4, __qtablewidgetitem70)
        __qtablewidgetitem71 = QTableWidgetItem()
        __qtablewidgetitem71.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(21, 5, __qtablewidgetitem71)
        __qtablewidgetitem72 = QTableWidgetItem()
        __qtablewidgetitem72.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(21, 6, __qtablewidgetitem72)
        __qtablewidgetitem73 = QTableWidgetItem()
        __qtablewidgetitem73.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(21, 7, __qtablewidgetitem73)
        __qtablewidgetitem74 = QTableWidgetItem()
        __qtablewidgetitem74.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(21, 8, __qtablewidgetitem74)
        __qtablewidgetitem75 = QTableWidgetItem()
        __qtablewidgetitem75.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(21, 9, __qtablewidgetitem75)
        __qtablewidgetitem76 = QTableWidgetItem()
        __qtablewidgetitem76.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(22, 0, __qtablewidgetitem76)
        __qtablewidgetitem77 = QTableWidgetItem()
        __qtablewidgetitem77.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(22, 1, __qtablewidgetitem77)
        __qtablewidgetitem78 = QTableWidgetItem()
        __qtablewidgetitem78.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(22, 2, __qtablewidgetitem78)
        __qtablewidgetitem79 = QTableWidgetItem()
        __qtablewidgetitem79.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(22, 3, __qtablewidgetitem79)
        __qtablewidgetitem80 = QTableWidgetItem()
        __qtablewidgetitem80.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(22, 4, __qtablewidgetitem80)
        __qtablewidgetitem81 = QTableWidgetItem()
        __qtablewidgetitem81.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(22, 5, __qtablewidgetitem81)
        __qtablewidgetitem82 = QTableWidgetItem()
        __qtablewidgetitem82.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(22, 6, __qtablewidgetitem82)
        __qtablewidgetitem83 = QTableWidgetItem()
        __qtablewidgetitem83.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(22, 7, __qtablewidgetitem83)
        __qtablewidgetitem84 = QTableWidgetItem()
        __qtablewidgetitem84.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(22, 8, __qtablewidgetitem84)
        __qtablewidgetitem85 = QTableWidgetItem()
        __qtablewidgetitem85.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(22, 9, __qtablewidgetitem85)
        __qtablewidgetitem86 = QTableWidgetItem()
        __qtablewidgetitem86.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(23, 0, __qtablewidgetitem86)
        __qtablewidgetitem87 = QTableWidgetItem()
        __qtablewidgetitem87.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(23, 1, __qtablewidgetitem87)
        __qtablewidgetitem88 = QTableWidgetItem()
        __qtablewidgetitem88.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(23, 2, __qtablewidgetitem88)
        __qtablewidgetitem89 = QTableWidgetItem()
        __qtablewidgetitem89.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(23, 3, __qtablewidgetitem89)
        __qtablewidgetitem90 = QTableWidgetItem()
        __qtablewidgetitem90.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(23, 4, __qtablewidgetitem90)
        __qtablewidgetitem91 = QTableWidgetItem()
        __qtablewidgetitem91.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(23, 5, __qtablewidgetitem91)
        __qtablewidgetitem92 = QTableWidgetItem()
        __qtablewidgetitem92.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(23, 6, __qtablewidgetitem92)
        __qtablewidgetitem93 = QTableWidgetItem()
        __qtablewidgetitem93.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(23, 7, __qtablewidgetitem93)
        __qtablewidgetitem94 = QTableWidgetItem()
        __qtablewidgetitem94.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(23, 8, __qtablewidgetitem94)
        __qtablewidgetitem95 = QTableWidgetItem()
        __qtablewidgetitem95.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(23, 9, __qtablewidgetitem95)
        __qtablewidgetitem96 = QTableWidgetItem()
        __qtablewidgetitem96.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(24, 0, __qtablewidgetitem96)
        __qtablewidgetitem97 = QTableWidgetItem()
        __qtablewidgetitem97.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(24, 1, __qtablewidgetitem97)
        __qtablewidgetitem98 = QTableWidgetItem()
        __qtablewidgetitem98.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(24, 2, __qtablewidgetitem98)
        __qtablewidgetitem99 = QTableWidgetItem()
        __qtablewidgetitem99.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(24, 3, __qtablewidgetitem99)
        __qtablewidgetitem100 = QTableWidgetItem()
        __qtablewidgetitem100.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(24, 4, __qtablewidgetitem100)
        __qtablewidgetitem101 = QTableWidgetItem()
        __qtablewidgetitem101.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(24, 5, __qtablewidgetitem101)
        __qtablewidgetitem102 = QTableWidgetItem()
        __qtablewidgetitem102.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(24, 6, __qtablewidgetitem102)
        __qtablewidgetitem103 = QTableWidgetItem()
        __qtablewidgetitem103.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(24, 7, __qtablewidgetitem103)
        __qtablewidgetitem104 = QTableWidgetItem()
        __qtablewidgetitem104.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(24, 8, __qtablewidgetitem104)
        __qtablewidgetitem105 = QTableWidgetItem()
        __qtablewidgetitem105.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(24, 9, __qtablewidgetitem105)
        __qtablewidgetitem106 = QTableWidgetItem()
        __qtablewidgetitem106.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(25, 0, __qtablewidgetitem106)
        __qtablewidgetitem107 = QTableWidgetItem()
        __qtablewidgetitem107.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(25, 1, __qtablewidgetitem107)
        __qtablewidgetitem108 = QTableWidgetItem()
        __qtablewidgetitem108.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(25, 2, __qtablewidgetitem108)
        __qtablewidgetitem109 = QTableWidgetItem()
        __qtablewidgetitem109.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(25, 3, __qtablewidgetitem109)
        __qtablewidgetitem110 = QTableWidgetItem()
        __qtablewidgetitem110.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(25, 4, __qtablewidgetitem110)
        __qtablewidgetitem111 = QTableWidgetItem()
        __qtablewidgetitem111.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(25, 5, __qtablewidgetitem111)
        __qtablewidgetitem112 = QTableWidgetItem()
        __qtablewidgetitem112.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(25, 6, __qtablewidgetitem112)
        __qtablewidgetitem113 = QTableWidgetItem()
        __qtablewidgetitem113.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(25, 7, __qtablewidgetitem113)
        __qtablewidgetitem114 = QTableWidgetItem()
        __qtablewidgetitem114.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(25, 8, __qtablewidgetitem114)
        __qtablewidgetitem115 = QTableWidgetItem()
        __qtablewidgetitem115.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(25, 9, __qtablewidgetitem115)
        __qtablewidgetitem116 = QTableWidgetItem()
        __qtablewidgetitem116.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(26, 0, __qtablewidgetitem116)
        __qtablewidgetitem117 = QTableWidgetItem()
        __qtablewidgetitem117.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(26, 1, __qtablewidgetitem117)
        __qtablewidgetitem118 = QTableWidgetItem()
        __qtablewidgetitem118.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(26, 2, __qtablewidgetitem118)
        __qtablewidgetitem119 = QTableWidgetItem()
        __qtablewidgetitem119.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(26, 3, __qtablewidgetitem119)
        __qtablewidgetitem120 = QTableWidgetItem()
        __qtablewidgetitem120.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(26, 4, __qtablewidgetitem120)
        __qtablewidgetitem121 = QTableWidgetItem()
        __qtablewidgetitem121.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(26, 5, __qtablewidgetitem121)
        __qtablewidgetitem122 = QTableWidgetItem()
        __qtablewidgetitem122.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(26, 6, __qtablewidgetitem122)
        __qtablewidgetitem123 = QTableWidgetItem()
        __qtablewidgetitem123.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(26, 7, __qtablewidgetitem123)
        __qtablewidgetitem124 = QTableWidgetItem()
        __qtablewidgetitem124.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(26, 8, __qtablewidgetitem124)
        __qtablewidgetitem125 = QTableWidgetItem()
        __qtablewidgetitem125.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(26, 9, __qtablewidgetitem125)
        self.tblitems_1.setObjectName(u"tblitems_1")
        self.tblitems_1.setGeometry(QRect(0, 0, 1481, 841))
        self.tblitems_1.setFont(font)
        self.tblitems_1.setLayoutDirection(Qt.LeftToRight)
        self.tblitems_1.setShowGrid(True)
        self.tblitems_1.setGridStyle(Qt.SolidLine)
        self.tblitems_1.setSortingEnabled(False)
        self.tblitems_1.setRowCount(27)
        self.tblitems_1.horizontalHeader().setVisible(True)
        self.tblitems_1.horizontalHeader().setCascadingSectionResizes(True)
        self.tblitems_1.horizontalHeader().setMinimumSectionSize(90)
        self.tblitems_1.horizontalHeader().setDefaultSectionSize(110)
        self.tblitems_1.horizontalHeader().setHighlightSections(True)
        self.tblitems_1.horizontalHeader().setProperty("showSortIndicator", True)
        self.tblitems_1.horizontalHeader().setStretchLastSection(True)
        self.tblitems_1.verticalHeader().setVisible(True)
        self.tblitems_1.verticalHeader().setCascadingSectionResizes(False)
        self.tblitems_1.verticalHeader().setHighlightSections(True)
        self.tblitems_1.verticalHeader().setProperty("showSortIndicator", False)
        self.tblitems_1.verticalHeader().setStretchLastSection(True)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tableView_plat_2 = QTableView(self.tab_3)
        self.tableView_plat_2.setObjectName(u"tableView_plat_2")
        self.tableView_plat_2.setGeometry(QRect(0, 0, 1401, 831))
        self.tableView_plat_2.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(234, 232, 220);\n"
"")
        self.tableView_plat_2.setLineWidth(3)
        self.tableView_plat_2.setMidLineWidth(2)
        self.tableView_plat_2.setSortingEnabled(True)
        self.tblitems_2 = QTableWidget(self.tab_3)
        if (self.tblitems_2.columnCount() < 10):
            self.tblitems_2.setColumnCount(10)
        __qtablewidgetitem126 = QTableWidgetItem()
        self.tblitems_2.setHorizontalHeaderItem(0, __qtablewidgetitem126)
        __qtablewidgetitem127 = QTableWidgetItem()
        self.tblitems_2.setHorizontalHeaderItem(1, __qtablewidgetitem127)
        __qtablewidgetitem128 = QTableWidgetItem()
        self.tblitems_2.setHorizontalHeaderItem(2, __qtablewidgetitem128)
        __qtablewidgetitem129 = QTableWidgetItem()
        self.tblitems_2.setHorizontalHeaderItem(3, __qtablewidgetitem129)
        __qtablewidgetitem130 = QTableWidgetItem()
        self.tblitems_2.setHorizontalHeaderItem(4, __qtablewidgetitem130)
        __qtablewidgetitem131 = QTableWidgetItem()
        self.tblitems_2.setHorizontalHeaderItem(5, __qtablewidgetitem131)
        __qtablewidgetitem132 = QTableWidgetItem()
        self.tblitems_2.setHorizontalHeaderItem(6, __qtablewidgetitem132)
        __qtablewidgetitem133 = QTableWidgetItem()
        self.tblitems_2.setHorizontalHeaderItem(7, __qtablewidgetitem133)
        __qtablewidgetitem134 = QTableWidgetItem()
        self.tblitems_2.setHorizontalHeaderItem(8, __qtablewidgetitem134)
        __qtablewidgetitem135 = QTableWidgetItem()
        self.tblitems_2.setHorizontalHeaderItem(9, __qtablewidgetitem135)
        if (self.tblitems_2.rowCount() < 27):
            self.tblitems_2.setRowCount(27)
        __qtablewidgetitem136 = QTableWidgetItem()
        __qtablewidgetitem136.setFont(font2);
        self.tblitems_2.setVerticalHeaderItem(0, __qtablewidgetitem136)
        __qtablewidgetitem137 = QTableWidgetItem()
        self.tblitems_2.setVerticalHeaderItem(1, __qtablewidgetitem137)
        __qtablewidgetitem138 = QTableWidgetItem()
        __qtablewidgetitem138.setFont(font2);
        self.tblitems_2.setVerticalHeaderItem(2, __qtablewidgetitem138)
        __qtablewidgetitem139 = QTableWidgetItem()
        self.tblitems_2.setVerticalHeaderItem(3, __qtablewidgetitem139)
        __qtablewidgetitem140 = QTableWidgetItem()
        self.tblitems_2.setVerticalHeaderItem(4, __qtablewidgetitem140)
        __qtablewidgetitem141 = QTableWidgetItem()
        self.tblitems_2.setVerticalHeaderItem(5, __qtablewidgetitem141)
        __qtablewidgetitem142 = QTableWidgetItem()
        self.tblitems_2.setVerticalHeaderItem(6, __qtablewidgetitem142)
        __qtablewidgetitem143 = QTableWidgetItem()
        __qtablewidgetitem143.setFont(font2);
        self.tblitems_2.setVerticalHeaderItem(7, __qtablewidgetitem143)
        __qtablewidgetitem144 = QTableWidgetItem()
        self.tblitems_2.setVerticalHeaderItem(8, __qtablewidgetitem144)
        __qtablewidgetitem145 = QTableWidgetItem()
        self.tblitems_2.setVerticalHeaderItem(9, __qtablewidgetitem145)
        __qtablewidgetitem146 = QTableWidgetItem()
        __qtablewidgetitem146.setText(u"\u0423\u0441\u0442\u0430\u0432\u043a\u0430 \u0441\u043e\u043f\u0440. \u0438\u0437\u043e\u043b\u044f\u0446\u0438\u0438 2 (\u041c\u041e\u043c)");
        __qtablewidgetitem146.setIcon(icon);
        self.tblitems_2.setVerticalHeaderItem(10, __qtablewidgetitem146)
        __qtablewidgetitem147 = QTableWidgetItem()
        self.tblitems_2.setVerticalHeaderItem(11, __qtablewidgetitem147)
        __qtablewidgetitem148 = QTableWidgetItem()
        __qtablewidgetitem148.setFont(font2);
        self.tblitems_2.setVerticalHeaderItem(12, __qtablewidgetitem148)
        __qtablewidgetitem149 = QTableWidgetItem()
        self.tblitems_2.setVerticalHeaderItem(13, __qtablewidgetitem149)
        __qtablewidgetitem150 = QTableWidgetItem()
        self.tblitems_2.setVerticalHeaderItem(14, __qtablewidgetitem150)
        __qtablewidgetitem151 = QTableWidgetItem()
        self.tblitems_2.setVerticalHeaderItem(15, __qtablewidgetitem151)
        __qtablewidgetitem152 = QTableWidgetItem()
        self.tblitems_2.setVerticalHeaderItem(16, __qtablewidgetitem152)
        __qtablewidgetitem153 = QTableWidgetItem()
        self.tblitems_2.setVerticalHeaderItem(17, __qtablewidgetitem153)
        __qtablewidgetitem154 = QTableWidgetItem()
        self.tblitems_2.setVerticalHeaderItem(18, __qtablewidgetitem154)
        __qtablewidgetitem155 = QTableWidgetItem()
        self.tblitems_2.setVerticalHeaderItem(19, __qtablewidgetitem155)
        __qtablewidgetitem156 = QTableWidgetItem()
        __qtablewidgetitem156.setFont(font2);
        self.tblitems_2.setVerticalHeaderItem(20, __qtablewidgetitem156)
        __qtablewidgetitem157 = QTableWidgetItem()
        self.tblitems_2.setVerticalHeaderItem(21, __qtablewidgetitem157)
        __qtablewidgetitem158 = QTableWidgetItem()
        self.tblitems_2.setVerticalHeaderItem(22, __qtablewidgetitem158)
        __qtablewidgetitem159 = QTableWidgetItem()
        self.tblitems_2.setVerticalHeaderItem(23, __qtablewidgetitem159)
        __qtablewidgetitem160 = QTableWidgetItem()
        self.tblitems_2.setVerticalHeaderItem(24, __qtablewidgetitem160)
        __qtablewidgetitem161 = QTableWidgetItem()
        self.tblitems_2.setVerticalHeaderItem(25, __qtablewidgetitem161)
        __qtablewidgetitem162 = QTableWidgetItem()
        self.tblitems_2.setVerticalHeaderItem(26, __qtablewidgetitem162)
        __qtablewidgetitem163 = QTableWidgetItem()
        __qtablewidgetitem163.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled|Qt.ItemIsAutoTristate);
        self.tblitems_2.setItem(9, 0, __qtablewidgetitem163)
        __qtablewidgetitem164 = QTableWidgetItem()
        __qtablewidgetitem164.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(21, 0, __qtablewidgetitem164)
        __qtablewidgetitem165 = QTableWidgetItem()
        __qtablewidgetitem165.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(21, 1, __qtablewidgetitem165)
        __qtablewidgetitem166 = QTableWidgetItem()
        __qtablewidgetitem166.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(21, 2, __qtablewidgetitem166)
        __qtablewidgetitem167 = QTableWidgetItem()
        __qtablewidgetitem167.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(21, 3, __qtablewidgetitem167)
        __qtablewidgetitem168 = QTableWidgetItem()
        __qtablewidgetitem168.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(21, 4, __qtablewidgetitem168)
        __qtablewidgetitem169 = QTableWidgetItem()
        __qtablewidgetitem169.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(21, 5, __qtablewidgetitem169)
        __qtablewidgetitem170 = QTableWidgetItem()
        __qtablewidgetitem170.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(21, 6, __qtablewidgetitem170)
        __qtablewidgetitem171 = QTableWidgetItem()
        __qtablewidgetitem171.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(21, 7, __qtablewidgetitem171)
        __qtablewidgetitem172 = QTableWidgetItem()
        __qtablewidgetitem172.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(21, 8, __qtablewidgetitem172)
        __qtablewidgetitem173 = QTableWidgetItem()
        __qtablewidgetitem173.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(21, 9, __qtablewidgetitem173)
        __qtablewidgetitem174 = QTableWidgetItem()
        __qtablewidgetitem174.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(22, 0, __qtablewidgetitem174)
        __qtablewidgetitem175 = QTableWidgetItem()
        __qtablewidgetitem175.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(22, 1, __qtablewidgetitem175)
        __qtablewidgetitem176 = QTableWidgetItem()
        __qtablewidgetitem176.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(22, 2, __qtablewidgetitem176)
        __qtablewidgetitem177 = QTableWidgetItem()
        __qtablewidgetitem177.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(22, 3, __qtablewidgetitem177)
        __qtablewidgetitem178 = QTableWidgetItem()
        __qtablewidgetitem178.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(22, 4, __qtablewidgetitem178)
        __qtablewidgetitem179 = QTableWidgetItem()
        __qtablewidgetitem179.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(22, 5, __qtablewidgetitem179)
        __qtablewidgetitem180 = QTableWidgetItem()
        __qtablewidgetitem180.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(22, 6, __qtablewidgetitem180)
        __qtablewidgetitem181 = QTableWidgetItem()
        __qtablewidgetitem181.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(22, 7, __qtablewidgetitem181)
        __qtablewidgetitem182 = QTableWidgetItem()
        __qtablewidgetitem182.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(22, 8, __qtablewidgetitem182)
        __qtablewidgetitem183 = QTableWidgetItem()
        __qtablewidgetitem183.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(22, 9, __qtablewidgetitem183)
        __qtablewidgetitem184 = QTableWidgetItem()
        __qtablewidgetitem184.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(23, 0, __qtablewidgetitem184)
        __qtablewidgetitem185 = QTableWidgetItem()
        __qtablewidgetitem185.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(23, 1, __qtablewidgetitem185)
        __qtablewidgetitem186 = QTableWidgetItem()
        __qtablewidgetitem186.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(23, 2, __qtablewidgetitem186)
        __qtablewidgetitem187 = QTableWidgetItem()
        __qtablewidgetitem187.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(23, 3, __qtablewidgetitem187)
        __qtablewidgetitem188 = QTableWidgetItem()
        __qtablewidgetitem188.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(23, 4, __qtablewidgetitem188)
        __qtablewidgetitem189 = QTableWidgetItem()
        __qtablewidgetitem189.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(23, 5, __qtablewidgetitem189)
        __qtablewidgetitem190 = QTableWidgetItem()
        __qtablewidgetitem190.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(23, 6, __qtablewidgetitem190)
        __qtablewidgetitem191 = QTableWidgetItem()
        __qtablewidgetitem191.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(23, 7, __qtablewidgetitem191)
        __qtablewidgetitem192 = QTableWidgetItem()
        __qtablewidgetitem192.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(23, 8, __qtablewidgetitem192)
        __qtablewidgetitem193 = QTableWidgetItem()
        __qtablewidgetitem193.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(23, 9, __qtablewidgetitem193)
        __qtablewidgetitem194 = QTableWidgetItem()
        __qtablewidgetitem194.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(24, 0, __qtablewidgetitem194)
        __qtablewidgetitem195 = QTableWidgetItem()
        __qtablewidgetitem195.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(24, 1, __qtablewidgetitem195)
        __qtablewidgetitem196 = QTableWidgetItem()
        __qtablewidgetitem196.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(24, 2, __qtablewidgetitem196)
        __qtablewidgetitem197 = QTableWidgetItem()
        __qtablewidgetitem197.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(24, 3, __qtablewidgetitem197)
        __qtablewidgetitem198 = QTableWidgetItem()
        __qtablewidgetitem198.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(24, 4, __qtablewidgetitem198)
        __qtablewidgetitem199 = QTableWidgetItem()
        __qtablewidgetitem199.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(24, 5, __qtablewidgetitem199)
        __qtablewidgetitem200 = QTableWidgetItem()
        __qtablewidgetitem200.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(24, 6, __qtablewidgetitem200)
        __qtablewidgetitem201 = QTableWidgetItem()
        __qtablewidgetitem201.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(24, 7, __qtablewidgetitem201)
        __qtablewidgetitem202 = QTableWidgetItem()
        __qtablewidgetitem202.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(24, 8, __qtablewidgetitem202)
        __qtablewidgetitem203 = QTableWidgetItem()
        __qtablewidgetitem203.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(24, 9, __qtablewidgetitem203)
        __qtablewidgetitem204 = QTableWidgetItem()
        __qtablewidgetitem204.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(25, 0, __qtablewidgetitem204)
        __qtablewidgetitem205 = QTableWidgetItem()
        __qtablewidgetitem205.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(25, 1, __qtablewidgetitem205)
        __qtablewidgetitem206 = QTableWidgetItem()
        __qtablewidgetitem206.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(25, 2, __qtablewidgetitem206)
        __qtablewidgetitem207 = QTableWidgetItem()
        __qtablewidgetitem207.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(25, 3, __qtablewidgetitem207)
        __qtablewidgetitem208 = QTableWidgetItem()
        __qtablewidgetitem208.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(25, 4, __qtablewidgetitem208)
        __qtablewidgetitem209 = QTableWidgetItem()
        __qtablewidgetitem209.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(25, 5, __qtablewidgetitem209)
        __qtablewidgetitem210 = QTableWidgetItem()
        __qtablewidgetitem210.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(25, 6, __qtablewidgetitem210)
        __qtablewidgetitem211 = QTableWidgetItem()
        __qtablewidgetitem211.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(25, 7, __qtablewidgetitem211)
        __qtablewidgetitem212 = QTableWidgetItem()
        __qtablewidgetitem212.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(25, 8, __qtablewidgetitem212)
        __qtablewidgetitem213 = QTableWidgetItem()
        __qtablewidgetitem213.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(25, 9, __qtablewidgetitem213)
        __qtablewidgetitem214 = QTableWidgetItem()
        __qtablewidgetitem214.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(26, 0, __qtablewidgetitem214)
        __qtablewidgetitem215 = QTableWidgetItem()
        __qtablewidgetitem215.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(26, 1, __qtablewidgetitem215)
        __qtablewidgetitem216 = QTableWidgetItem()
        __qtablewidgetitem216.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(26, 2, __qtablewidgetitem216)
        __qtablewidgetitem217 = QTableWidgetItem()
        __qtablewidgetitem217.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(26, 3, __qtablewidgetitem217)
        __qtablewidgetitem218 = QTableWidgetItem()
        __qtablewidgetitem218.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(26, 4, __qtablewidgetitem218)
        __qtablewidgetitem219 = QTableWidgetItem()
        __qtablewidgetitem219.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(26, 5, __qtablewidgetitem219)
        __qtablewidgetitem220 = QTableWidgetItem()
        __qtablewidgetitem220.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(26, 6, __qtablewidgetitem220)
        __qtablewidgetitem221 = QTableWidgetItem()
        __qtablewidgetitem221.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(26, 7, __qtablewidgetitem221)
        __qtablewidgetitem222 = QTableWidgetItem()
        __qtablewidgetitem222.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(26, 8, __qtablewidgetitem222)
        __qtablewidgetitem223 = QTableWidgetItem()
        __qtablewidgetitem223.setTextAlignment(Qt.AlignCenter);
        self.tblitems_2.setItem(26, 9, __qtablewidgetitem223)
        self.tblitems_2.setObjectName(u"tblitems_2")
        self.tblitems_2.setGeometry(QRect(0, 0, 1481, 841))
        self.tblitems_2.setFont(font)
        self.tblitems_2.setLayoutDirection(Qt.LeftToRight)
        self.tblitems_2.setShowGrid(True)
        self.tblitems_2.setGridStyle(Qt.SolidLine)
        self.tblitems_2.setSortingEnabled(False)
        self.tblitems_2.setRowCount(27)
        self.tblitems_2.horizontalHeader().setVisible(True)
        self.tblitems_2.horizontalHeader().setCascadingSectionResizes(True)
        self.tblitems_2.horizontalHeader().setMinimumSectionSize(90)
        self.tblitems_2.horizontalHeader().setDefaultSectionSize(110)
        self.tblitems_2.horizontalHeader().setHighlightSections(True)
        self.tblitems_2.horizontalHeader().setProperty("showSortIndicator", True)
        self.tblitems_2.horizontalHeader().setStretchLastSection(True)
        self.tblitems_2.verticalHeader().setVisible(True)
        self.tblitems_2.verticalHeader().setCascadingSectionResizes(False)
        self.tblitems_2.verticalHeader().setHighlightSections(True)
        self.tblitems_2.verticalHeader().setProperty("showSortIndicator", False)
        self.tblitems_2.verticalHeader().setStretchLastSection(True)
        self.tabWidget.addTab(self.tab_3, "")

        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.tabWidget.setToolTip("")
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem = self.tableWidget_PMK.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435", None));
        ___qtablewidgetitem1 = self.tableWidget_PMK.verticalHeaderItem(0)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0436\u0438\u043c \u0440\u0430\u0431\u043e\u0442\u044b \u043f\u0440\u0438\u0431\u043e\u0440\u0430", None));
        ___qtablewidgetitem2 = self.tableWidget_PMK.verticalHeaderItem(1)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u043c\u0435\u0440 \u0432\u0435\u0440\u0441\u0438\u0438 \u041f\u041e", None));
        ___qtablewidgetitem3 = self.tableWidget_PMK.verticalHeaderItem(2)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"ID \u0448\u0430\u0441\u0441\u0438", None));
        ___qtablewidgetitem4 = self.tableWidget_PMK.verticalHeaderItem(3)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"ID \u041f\u043b\u0430\u0442\u044b 1", None));
        ___qtablewidgetitem5 = self.tableWidget_PMK.verticalHeaderItem(4)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"ID \u041f\u043b\u0430\u0442\u044b 2", None));
        ___qtablewidgetitem6 = self.tableWidget_PMK.verticalHeaderItem(5)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043d\u0442\u0440\u043e\u043b\u044c\u043d\u0430\u044f \u0441\u0443\u043c\u043c\u0430 \u041f\u041e MD5", None));

        __sortingEnabled = self.tableWidget_PMK.isSortingEnabled()
        self.tableWidget_PMK.setSortingEnabled(False)
        ___qtablewidgetitem7 = self.tableWidget_PMK.item(0, 0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"AA22", None));
        self.tableWidget_PMK.setSortingEnabled(__sortingEnabled)

        self.label_info.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.comboBox_1.setItemText(0, QCoreApplication.translate("MainWindow", u"0", None))
        self.comboBox_1.setItemText(1, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox_1.setItemText(2, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBox_1.setItemText(3, QCoreApplication.translate("MainWindow", u"3", None))
        self.comboBox_1.setItemText(4, QCoreApplication.translate("MainWindow", u"4", None))
        self.comboBox_1.setItemText(5, QCoreApplication.translate("MainWindow", u"5", None))
        self.comboBox_1.setItemText(6, QCoreApplication.translate("MainWindow", u"6", None))
        self.comboBox_1.setItemText(7, QCoreApplication.translate("MainWindow", u"7", None))
        self.comboBox_1.setItemText(8, QCoreApplication.translate("MainWindow", u"8", None))
        self.comboBox_1.setItemText(9, QCoreApplication.translate("MainWindow", u"9", None))
        self.comboBox_1.setItemText(10, QCoreApplication.translate("MainWindow", u"a", None))
        self.comboBox_1.setItemText(11, QCoreApplication.translate("MainWindow", u"b", None))
        self.comboBox_1.setItemText(12, QCoreApplication.translate("MainWindow", u"c", None))
        self.comboBox_1.setItemText(13, QCoreApplication.translate("MainWindow", u"d", None))
        self.comboBox_1.setItemText(14, QCoreApplication.translate("MainWindow", u"e", None))
        self.comboBox_1.setItemText(15, QCoreApplication.translate("MainWindow", u"f", None))

        self.Button_con.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u043a\u043b\u044e\u0447\u0438\u0442\u044c", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u043c\u0435\u0440 \u0443\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432\u0430 \u043d\u0430 \u0448\u0438\u043d\u0435 Modbus", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"5", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"9", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"d", None))

        ___qtablewidgetitem8 = self.tblitems_d.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043d\u0430\u043b 1", None));
        ___qtablewidgetitem9 = self.tblitems_d.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043d\u0430\u043b 2", None));
        ___qtablewidgetitem10 = self.tblitems_d.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043d\u0430\u043b 3", None));
        ___qtablewidgetitem11 = self.tblitems_d.horizontalHeaderItem(3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043d\u0430\u043b 4", None));
        ___qtablewidgetitem12 = self.tblitems_d.horizontalHeaderItem(4)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043d\u0430\u043b 5", None));
        ___qtablewidgetitem13 = self.tblitems_d.horizontalHeaderItem(5)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043d\u0430\u043b 6", None));
        ___qtablewidgetitem14 = self.tblitems_d.horizontalHeaderItem(6)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043d\u0430\u043b 7", None));
        ___qtablewidgetitem15 = self.tblitems_d.horizontalHeaderItem(7)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043d\u0430\u043b 8", None));
        ___qtablewidgetitem16 = self.tblitems_d.horizontalHeaderItem(8)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043d\u0430\u043b 9", None));
        ___qtablewidgetitem17 = self.tblitems_d.horizontalHeaderItem(9)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043d\u0430\u043b 10", None));
        ___qtablewidgetitem18 = self.tblitems_d.verticalHeaderItem(0)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043b\u0430\u0442\u0430 1;", None));
        ___qtablewidgetitem19 = self.tblitems_d.verticalHeaderItem(1)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0438\u0441\u043f\u0440\u0430\u0432\u043d\u043e\u0432\u0442\u044c \u0410\u0426\u041f", None));
        ___qtablewidgetitem20 = self.tblitems_d.verticalHeaderItem(2)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0438\u0441\u043f\u0440\u0430\u0432\u043d\u043e\u0441\u0442\u044c \u0441\u043c\u0435\u0449\u0435\u043d\u0438\u044f +100 \u0412", None));
        ___qtablewidgetitem21 = self.tblitems_d.verticalHeaderItem(3)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0438\u0441\u043f\u0440\u0430\u0432\u043d\u043e\u0441\u0442\u044c \u0441\u043c\u0435\u0449\u0435\u043d\u0438\u044f -100 \u0412", None));
        ___qtablewidgetitem22 = self.tblitems_d.verticalHeaderItem(4)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043b\u0430\u0442\u0430 2:", None));
        ___qtablewidgetitem23 = self.tblitems_d.verticalHeaderItem(5)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0438\u0441\u043f\u0440\u0430\u0432\u043d\u043e\u0432\u0442\u044c \u0410\u0426\u041f", None));
        ___qtablewidgetitem24 = self.tblitems_d.verticalHeaderItem(6)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0438\u0441\u043f\u0440\u0430\u0432\u043d\u043e\u0441\u0442\u044c \u0441\u043c\u0435\u0449\u0435\u043d\u0438\u044f +100 \u0412", None));

        __sortingEnabled1 = self.tblitems_d.isSortingEnabled()
        self.tblitems_d.setSortingEnabled(False)
        self.tblitems_d.setSortingEnabled(__sortingEnabled1)

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0430\u0433\u043d\u043e\u0441\u0442\u0438\u043a\u0430 \u041f\u041c\u041a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QCoreApplication.translate("MainWindow", u"\u041f\u041c\u041a-20", None))
        ___qtablewidgetitem25 = self.tblitems_1.horizontalHeaderItem(0)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043d\u0430\u043b 1", None));
        ___qtablewidgetitem26 = self.tblitems_1.horizontalHeaderItem(1)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043d\u0430\u043b 2", None));
        ___qtablewidgetitem27 = self.tblitems_1.horizontalHeaderItem(2)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043d\u0430\u043b 3", None));
        ___qtablewidgetitem28 = self.tblitems_1.horizontalHeaderItem(3)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043d\u0430\u043b 4", None));
        ___qtablewidgetitem29 = self.tblitems_1.horizontalHeaderItem(4)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043d\u0430\u043b 5", None));
        ___qtablewidgetitem30 = self.tblitems_1.horizontalHeaderItem(5)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043d\u0430\u043b 6", None));
        ___qtablewidgetitem31 = self.tblitems_1.horizontalHeaderItem(6)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043d\u0430\u043b 7", None));
        ___qtablewidgetitem32 = self.tblitems_1.horizontalHeaderItem(7)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043d\u0430\u043b 8", None));
        ___qtablewidgetitem33 = self.tblitems_1.horizontalHeaderItem(8)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043d\u0430\u043b 9", None));
        ___qtablewidgetitem34 = self.tblitems_1.horizontalHeaderItem(9)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043d\u0430\u043b 10", None));
        ___qtablewidgetitem35 = self.tblitems_1.verticalHeaderItem(0)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0436\u0438\u043c\u044b \u0440\u0430\u0431\u043e\u0442\u044b:", None));
        ___qtablewidgetitem36 = self.tblitems_1.verticalHeaderItem(1)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u043d\u0438\u0442\u043e\u0440\u0438\u043d\u0433 \u043a\u0430\u0431\u0435\u043b\u044f", None));
        ___qtablewidgetitem37 = self.tblitems_1.verticalHeaderItem(2)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043f\u0443\u0441\u0442\u0438\u043c\u044b\u0435 \u0434\u0438\u0430\u043f\u0430\u0437\u043e\u043d\u044b:", None));
        ___qtablewidgetitem38 = self.tblitems_1.verticalHeaderItem(3)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0430\u043f\u0430\u0437\u043e\u043d \u0441\u043e\u043f\u0440. \u0438\u0437\u043e\u043b\u044f\u0446\u0438\u0438 \u0430\u0432\u0430\u0440. ", None));
        ___qtablewidgetitem39 = self.tblitems_1.verticalHeaderItem(4)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0430\u043f\u0430\u0437\u043e\u043d \u0441\u043e\u043f\u0440. \u0448\u043b\u0435\u0439\u0444\u0430 \u0430\u0432\u0430\u0440.", None));
        ___qtablewidgetitem40 = self.tblitems_1.verticalHeaderItem(5)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0430\u043f\u0430\u0437\u043e\u043d \u0441\u043e\u043f\u0440. \u0438\u0437\u043e\u043b\u044f\u0446\u0438\u0438 \u043f\u0440\u0435\u0434\u0443\u043f\u0440.", None));
        ___qtablewidgetitem41 = self.tblitems_1.verticalHeaderItem(6)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0430\u043f\u0430\u0437\u043e\u043d \u0441\u043e\u043f\u0440. \u0448\u043b\u0435\u0439\u0444\u0430 \u043f\u0440\u0435\u0434\u0443\u043f\u0440.", None));
        ___qtablewidgetitem42 = self.tblitems_1.verticalHeaderItem(7)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0441\u0442\u0430\u0432\u043a\u0438:", None));
        ___qtablewidgetitem43 = self.tblitems_1.verticalHeaderItem(8)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0441\u0442\u0430\u0432\u043a\u0430 \u043d\u0430\u043f\u0440\u044f\u0436\u0435\u043d\u0438\u044f \u043d\u0430 \u0432\u0445\u043e\u0434\u0435 (\u0412)", None));
        ___qtablewidgetitem44 = self.tblitems_1.verticalHeaderItem(9)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0441\u0442\u0430\u0432\u043a\u0430 \u0441\u043e\u043f\u0440. \u0438\u0437\u043e\u043b\u044f\u0446\u0438\u0438 1 (\u041c\u041e\u043c)", None));
        ___qtablewidgetitem45 = self.tblitems_1.verticalHeaderItem(11)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0441\u0442\u0430\u0432\u043a\u0430 \u0441\u043e\u043f\u0440. \u0448\u043b\u0435\u0439\u0444\u0430 (\u043a\u041e\u043c)", None));
        ___qtablewidgetitem46 = self.tblitems_1.verticalHeaderItem(12)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043a\u0443\u0449\u0438\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f:", None));
        ___qtablewidgetitem47 = self.tblitems_1.verticalHeaderItem(13)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u043f\u0440. \u0438\u0437\u043e\u043b\u044f\u0446\u0438\u0438 1 (\u041c\u041e\u043c)", None));
        ___qtablewidgetitem48 = self.tblitems_1.verticalHeaderItem(14)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u043f\u0440. \u0438\u0437\u043e\u043b\u044f\u0446\u0438\u0438 2 (\u041c\u041e\u043c)", None));
        ___qtablewidgetitem49 = self.tblitems_1.verticalHeaderItem(15)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u043f\u0440. \u0448\u043b\u0435\u0439\u0444\u0430 (\u043a\u041e\u043c)", None));
        ___qtablewidgetitem50 = self.tblitems_1.verticalHeaderItem(16)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u043f\u0440\u044f\u0436\u0435\u043d\u0438\u0435 \u043d\u0430 \u0432\u0445\u043e\u0434\u0435 1 (\u0412)", None));
        ___qtablewidgetitem51 = self.tblitems_1.verticalHeaderItem(17)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u043f\u0440\u044f\u0436\u0435\u043d\u0438\u0435 \u043d\u0430 \u0432\u0445\u043e\u0434\u0435 2 (\u0412)", None));
        ___qtablewidgetitem52 = self.tblitems_1.verticalHeaderItem(18)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0447\u0435\u0442\u043d\u043e\u0435 \u0437\u043d\u0430\u0447. \u043e\u0431\u044a\u0435\u043c. \u043d\u0430\u043f\u0440\u044f\u0436\u0435\u043d\u0438\u044f 1 (\u0412)", None));
        ___qtablewidgetitem53 = self.tblitems_1.verticalHeaderItem(19)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0447\u0435\u0442\u043d\u043e\u0435 \u0437\u043d\u0430\u0447. \u043e\u0431\u044a\u0435\u043c. \u043d\u0430\u043f\u0440\u044f\u0436\u0435\u043d\u0438\u044f 2 (\u0412)", None));
        ___qtablewidgetitem54 = self.tblitems_1.verticalHeaderItem(20)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0430\u0440\u0438\u0439\u043d\u044b\u0435 \u0441\u0438\u0433\u043d\u0430\u043b\u044b\":", None));
        ___qtablewidgetitem55 = self.tblitems_1.verticalHeaderItem(21)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u043f\u0440\u043e\u0442\u0438\u0432\u043b\u0435\u043d\u0438\u0435 \u0438\u0437\u043e\u043b\u044f\u0446\u0438\u0438 1 < \u0434\u043e\u043f.", None));
        ___qtablewidgetitem56 = self.tblitems_1.verticalHeaderItem(22)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u043f\u0440\u043e\u0442\u0438\u0432\u043b\u0435\u043d\u0438\u0435 \u0438\u0437\u043e\u043b\u044f\u0446\u0438\u0438 2 < \u0434\u043e\u043f.", None));
        ___qtablewidgetitem57 = self.tblitems_1.verticalHeaderItem(23)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u043f\u0440\u043e\u0442\u0438\u0432\u043b\u0435\u043d\u0438\u0435 \u0448\u043b\u0435\u0439\u0444\u0430 < \u0434\u043e\u043f.", None));
        ___qtablewidgetitem58 = self.tblitems_1.verticalHeaderItem(24)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u043f\u0440\u043e\u0442\u0438\u0432\u043b\u0435\u043d\u0438\u0435 \u0448\u043b\u0435\u0439\u0444\u0430 > \u0434\u043e\u043f.", None));
        ___qtablewidgetitem59 = self.tblitems_1.verticalHeaderItem(25)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u043f\u0440\u044f\u0436\u0435\u043d\u0438\u0435 1 \u0432\u044b\u0448\u0435 \u0434\u043e\u043f\u0443\u0441\u043a", None));
        ___qtablewidgetitem60 = self.tblitems_1.verticalHeaderItem(26)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u043f\u0440\u044f\u0436\u0435\u043d\u0438\u0435 2 \u0432\u044b\u0448\u0435 \u0434\u043e\u043f\u0443\u0441\u043a", None));

        __sortingEnabled2 = self.tblitems_1.isSortingEnabled()
        self.tblitems_1.setSortingEnabled(False)
        self.tblitems_1.setSortingEnabled(__sortingEnabled2)

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u041f\u043b\u0430\u0442\u0430 1", None))
        ___qtablewidgetitem61 = self.tblitems_2.horizontalHeaderItem(0)
        ___qtablewidgetitem61.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043d\u0430\u043b 1", None));
        ___qtablewidgetitem62 = self.tblitems_2.horizontalHeaderItem(1)
        ___qtablewidgetitem62.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043d\u0430\u043b 2", None));
        ___qtablewidgetitem63 = self.tblitems_2.horizontalHeaderItem(2)
        ___qtablewidgetitem63.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043d\u0430\u043b 3", None));
        ___qtablewidgetitem64 = self.tblitems_2.horizontalHeaderItem(3)
        ___qtablewidgetitem64.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043d\u0430\u043b 4", None));
        ___qtablewidgetitem65 = self.tblitems_2.horizontalHeaderItem(4)
        ___qtablewidgetitem65.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043d\u0430\u043b 5", None));
        ___qtablewidgetitem66 = self.tblitems_2.horizontalHeaderItem(5)
        ___qtablewidgetitem66.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043d\u0430\u043b 6", None));
        ___qtablewidgetitem67 = self.tblitems_2.horizontalHeaderItem(6)
        ___qtablewidgetitem67.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043d\u0430\u043b 7", None));
        ___qtablewidgetitem68 = self.tblitems_2.horizontalHeaderItem(7)
        ___qtablewidgetitem68.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043d\u0430\u043b 8", None));
        ___qtablewidgetitem69 = self.tblitems_2.horizontalHeaderItem(8)
        ___qtablewidgetitem69.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043d\u0430\u043b 9", None));
        ___qtablewidgetitem70 = self.tblitems_2.horizontalHeaderItem(9)
        ___qtablewidgetitem70.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043d\u0430\u043b 10", None));
        ___qtablewidgetitem71 = self.tblitems_2.verticalHeaderItem(0)
        ___qtablewidgetitem71.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0436\u0438\u043c\u044b \u0440\u0430\u0431\u043e\u0442\u044b:", None));
        ___qtablewidgetitem72 = self.tblitems_2.verticalHeaderItem(1)
        ___qtablewidgetitem72.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u043d\u0438\u0442\u043e\u0440\u0438\u043d\u0433 \u043a\u0430\u0431\u0435\u043b\u044f", None));
        ___qtablewidgetitem73 = self.tblitems_2.verticalHeaderItem(2)
        ___qtablewidgetitem73.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043f\u0443\u0441\u0442\u0438\u043c\u044b\u0435 \u0434\u0438\u0430\u043f\u0430\u0437\u043e\u043d\u044b:", None));
        ___qtablewidgetitem74 = self.tblitems_2.verticalHeaderItem(3)
        ___qtablewidgetitem74.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0430\u043f\u0430\u0437\u043e\u043d \u0441\u043e\u043f\u0440. \u0438\u0437\u043e\u043b\u044f\u0446\u0438\u0438 \u0430\u0432\u0430\u0440. ", None));
        ___qtablewidgetitem75 = self.tblitems_2.verticalHeaderItem(4)
        ___qtablewidgetitem75.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0430\u043f\u0430\u0437\u043e\u043d \u0441\u043e\u043f\u0440. \u0448\u043b\u0435\u0439\u0444\u0430 \u0430\u0432\u0430\u0440.", None));
        ___qtablewidgetitem76 = self.tblitems_2.verticalHeaderItem(5)
        ___qtablewidgetitem76.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0430\u043f\u0430\u0437\u043e\u043d \u0441\u043e\u043f\u0440. \u0438\u0437\u043e\u043b\u044f\u0446\u0438\u0438 \u043f\u0440\u0435\u0434\u0443\u043f\u0440.", None));
        ___qtablewidgetitem77 = self.tblitems_2.verticalHeaderItem(6)
        ___qtablewidgetitem77.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0430\u043f\u0430\u0437\u043e\u043d \u0441\u043e\u043f\u0440. \u0448\u043b\u0435\u0439\u0444\u0430 \u043f\u0440\u0435\u0434\u0443\u043f\u0440.", None));
        ___qtablewidgetitem78 = self.tblitems_2.verticalHeaderItem(7)
        ___qtablewidgetitem78.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0441\u0442\u0430\u0432\u043a\u0438:", None));
        ___qtablewidgetitem79 = self.tblitems_2.verticalHeaderItem(8)
        ___qtablewidgetitem79.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0441\u0442\u0430\u0432\u043a\u0430 \u043d\u0430\u043f\u0440\u044f\u0436\u0435\u043d\u0438\u044f \u043d\u0430 \u0432\u0445\u043e\u0434\u0435 (\u0412)", None));
        ___qtablewidgetitem80 = self.tblitems_2.verticalHeaderItem(9)
        ___qtablewidgetitem80.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0441\u0442\u0430\u0432\u043a\u0430 \u0441\u043e\u043f\u0440. \u0438\u0437\u043e\u043b\u044f\u0446\u0438\u0438 1 (\u041c\u041e\u043c)", None));
        ___qtablewidgetitem81 = self.tblitems_2.verticalHeaderItem(11)
        ___qtablewidgetitem81.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0441\u0442\u0430\u0432\u043a\u0430 \u0441\u043e\u043f\u0440. \u0448\u043b\u0435\u0439\u0444\u0430 (\u043a\u041e\u043c)", None));
        ___qtablewidgetitem82 = self.tblitems_2.verticalHeaderItem(12)
        ___qtablewidgetitem82.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043a\u0443\u0449\u0438\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f:", None));
        ___qtablewidgetitem83 = self.tblitems_2.verticalHeaderItem(13)
        ___qtablewidgetitem83.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u043f\u0440. \u0438\u0437\u043e\u043b\u044f\u0446\u0438\u0438 1 (\u041c\u041e\u043c)", None));
        ___qtablewidgetitem84 = self.tblitems_2.verticalHeaderItem(14)
        ___qtablewidgetitem84.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u043f\u0440. \u0438\u0437\u043e\u043b\u044f\u0446\u0438\u0438 2 (\u041c\u041e\u043c)", None));
        ___qtablewidgetitem85 = self.tblitems_2.verticalHeaderItem(15)
        ___qtablewidgetitem85.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u043f\u0440. \u0448\u043b\u0435\u0439\u0444\u0430 (\u043a\u041e\u043c)", None));
        ___qtablewidgetitem86 = self.tblitems_2.verticalHeaderItem(16)
        ___qtablewidgetitem86.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u043f\u0440\u044f\u0436\u0435\u043d\u0438\u0435 \u043d\u0430 \u0432\u0445\u043e\u0434\u0435 1 (\u0412)", None));
        ___qtablewidgetitem87 = self.tblitems_2.verticalHeaderItem(17)
        ___qtablewidgetitem87.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u043f\u0440\u044f\u0436\u0435\u043d\u0438\u0435 \u043d\u0430 \u0432\u0445\u043e\u0434\u0435 2 (\u0412)", None));
        ___qtablewidgetitem88 = self.tblitems_2.verticalHeaderItem(18)
        ___qtablewidgetitem88.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0447\u0435\u0442\u043d\u043e\u0435 \u0437\u043d\u0430\u0447. \u043e\u0431\u044a\u0435\u043c. \u043d\u0430\u043f\u0440\u044f\u0436\u0435\u043d\u0438\u044f 1 (\u0412)", None));
        ___qtablewidgetitem89 = self.tblitems_2.verticalHeaderItem(19)
        ___qtablewidgetitem89.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0447\u0435\u0442\u043d\u043e\u0435 \u0437\u043d\u0430\u0447. \u043e\u0431\u044a\u0435\u043c. \u043d\u0430\u043f\u0440\u044f\u0436\u0435\u043d\u0438\u044f 2 (\u0412)", None));
        ___qtablewidgetitem90 = self.tblitems_2.verticalHeaderItem(20)
        ___qtablewidgetitem90.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0430\u0440\u0438\u0439\u043d\u044b\u0435 \u0441\u0438\u0433\u043d\u0430\u043b\u044b\":", None));
        ___qtablewidgetitem91 = self.tblitems_2.verticalHeaderItem(21)
        ___qtablewidgetitem91.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u043f\u0440\u043e\u0442\u0438\u0432\u043b\u0435\u043d\u0438\u0435 \u0438\u0437\u043e\u043b\u044f\u0446\u0438\u0438 1 < \u0434\u043e\u043f.", None));
        ___qtablewidgetitem92 = self.tblitems_2.verticalHeaderItem(22)
        ___qtablewidgetitem92.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u043f\u0440\u043e\u0442\u0438\u0432\u043b\u0435\u043d\u0438\u0435 \u0438\u0437\u043e\u043b\u044f\u0446\u0438\u0438 2 < \u0434\u043e\u043f.", None));
        ___qtablewidgetitem93 = self.tblitems_2.verticalHeaderItem(23)
        ___qtablewidgetitem93.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u043f\u0440\u043e\u0442\u0438\u0432\u043b\u0435\u043d\u0438\u0435 \u0448\u043b\u0435\u0439\u0444\u0430 < \u0434\u043e\u043f.", None));
        ___qtablewidgetitem94 = self.tblitems_2.verticalHeaderItem(24)
        ___qtablewidgetitem94.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u043f\u0440\u043e\u0442\u0438\u0432\u043b\u0435\u043d\u0438\u0435 \u0448\u043b\u0435\u0439\u0444\u0430 > \u0434\u043e\u043f.", None));
        ___qtablewidgetitem95 = self.tblitems_2.verticalHeaderItem(25)
        ___qtablewidgetitem95.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u043f\u0440\u044f\u0436\u0435\u043d\u0438\u0435 1 \u0432\u044b\u0448\u0435 \u0434\u043e\u043f\u0443\u0441\u043a", None));
        ___qtablewidgetitem96 = self.tblitems_2.verticalHeaderItem(26)
        ___qtablewidgetitem96.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u043f\u0440\u044f\u0436\u0435\u043d\u0438\u0435 2 \u0432\u044b\u0448\u0435 \u0434\u043e\u043f\u0443\u0441\u043a", None));

        __sortingEnabled3 = self.tblitems_2.isSortingEnabled()
        self.tblitems_2.setSortingEnabled(False)
        self.tblitems_2.setSortingEnabled(__sortingEnabled3)

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u041f\u043b\u0430\u0442\u0430 2", None))
    # retranslateUi





def byte_to_bit (byte, bit):
	out = ((byte>>bit) & 1)
	return out

class myModbus():
	def __init__(self):
		self._dataP1 = None
		self._dataP2 = None
		self._dataP3 = None
		self._dataP4 = None

	def setDataP1(self, dataP1):
		self._dataP1 = dataP1

	def getDataP1(self):
		return self._dataP1

	def setDataP2(self, dataP2):
		self._dataP2 = dataP2

	def getDataP2(self):
		return self._dataP2

	def setDataP3(self, dataP3):
		self._dataP3 = dataP3

	def getDataP3(self):
		return self._dataP3

	def setDataP4(self, dataP4):
		self._dataP4 = dataP4

	def getDataP4(self):
		return self._dataP4

	def con_1(self):

		try:
			instrument = minimalmodbus.Instrument('/dev/ttyUSB0', int(self._dataP4[0][0]))
			instrument.serial.baudrate = 9600
			instrument.serial.timeout = 1.0
			instrument.mode = minimalmodbus.MODE_RTU

		# instrument.close_port_after_each_call = True
		except Exception as error:
			print ("[!] Exception occurred: ", error)
			# errorcounter = errorcounter + 1
			print("Ошибка подключения по RS-485_2 IOError ")
			# instrument.close_port_after_each_call = True
			self._dataP4[4][0] = 1 # Ошибка подключения по RS-485
			# time.sleep(5)
		# except (FileNotFoundError, IOError, RuntimeError, TypeError, NameError, IndexError):
		# 	print("Ошибка подключения по RS-485_2 - File Not Found")
		# 	instrument.close_port_after_each_call = True
		# except (IOError, RuntimeError, TypeError, NameError, UnboundLocalError, FileNotFoundError):
		# 	print("Ошибка подключения по RS-485_2 ")
		# 	instrument.close_port_after_each_call = True
		# instrument.serial.close()
		else:
			self._dataP4[4][0] = 0
			# self._dataP4[5][0] = 0
			# self._dataP4[5][1] = 0

			# print("Подключение по RS - 485 выполнено")
			try:
				""""
				режим ПМК
				"""
				modePmk1 = instrument.read_register(registeraddress = 145)
				self._dataP4[1][1] = modePmk1
				""""
				Номер версии ПО
				"""
				Nversion = instrument.read_registers(registeraddress = 90, number_of_registers = 2)
				self._dataP4[1][2] = (Nversion[0] * 65536 + Nversion[1])

				# print('NVERSION = ', self._dataP4[1][2])
				instrument.close_port_after_each_call = True
				""""
				ID шасси
				"""
				IDpmk1 = instrument.read_registers(registeraddress = 110, number_of_registers = 2)
				self._dataP4[1][3] = (IDpmk1[0] * 65536 + IDpmk1[1])
				""""
				ID платы измерения 1
				"""
				IDpi1 = instrument.read_registers(registeraddress = 100, number_of_registers = 6)
				self._dataP4[1][4] = IDpi1[0]
				self._dataP4[1][5] = IDpi1[1]
				self._dataP4[1][6] = IDpi1[2]
				self._dataP4[1][7] = IDpi1[3]
				self._dataP4[1][8] = IDpi1[4]
				self._dataP4[1][9] = IDpi1[5]
				"""
				Контрольная сумма ПО md5
				"""
				md5 = instrument.read_registers(registeraddress = 120, number_of_registers = 8)
				self._dataP4[2][0] = md5[0]
				self._dataP4[2][1] = md5[1]
				self._dataP4[2][2] = md5[2]
				self._dataP4[2][3] = md5[3]
				self._dataP4[2][4] = md5[4]
				self._dataP4[2][5] = md5[5]
				self._dataP4[2][6] = md5[6]
				self._dataP4[2][7] = md5[7]
				"""
				Режим старта
				"""
				modeStart1 = instrument.read_bit(registeraddress = 200)
				self._dataP4[3][0] = modeStart1
				""""
				Плата 1 режим работы канала
				"""
				modeCh1 = instrument.read_registers(registeraddress = 40, number_of_registers = 10)
				self._dataP1[0] = modeCh1
				""""
				Плата 1 Диапазон сопротивления изоляции аварийный
				"""
				deltaAV = instrument.read_registers(registeraddress = 0, number_of_registers = 10)
				for i in range(10):
					self._dataP1[1][i] = deltaAV[i] >> 8
				""""
				Плата 1 Диапазон сопротивления шлейфа аварийный
				"""
				for i in range(10):
					self._dataP1[2][i] = deltaAV[i] & 0x00FF
				""""
				Плата 1 Диапазон сопротивления изоляции предупредительный
				"""
				deltaAV = instrument.read_registers(registeraddress = 250, number_of_registers = 10)
				for i in range(10):
					self._dataP1[3][i] = deltaAV[i] >> 8
				""""
				Плата 1 Диапазон сопротивления шлейфа предупредительный
				"""
				for i in range(10):
					self._dataP1[4][i] = deltaAV[i] & 0x00FF
				""""
				Плата 1 Допустимое значение напряжения на входе В.
				"""
				deltaAV = instrument.read_registers(registeraddress = 200, number_of_registers = 10)
				self._dataP1[5] = deltaAV
				""""
				Плата 1 Уставка сопротивления изоляции 1 (MОм).
				"""
				deltaAV = instrument.read_registers(registeraddress = 10, number_of_registers = 10)
				for i in range(10):
					self._dataP1[6][i] = round((deltaAV[i] * 16 / 1000), 2)
				"""
				Плата 1 Уставка сопротивления изоляции 2 (MОм).
				"""
				deltaAV = instrument.read_registers(registeraddress = 20, number_of_registers = 10)
				for i in range(10):
					self._dataP1[7][i] = round((deltaAV[i] * 16 / 1000), 2)
				"""
				Плата 1 Уставка сопротивления шлейфа (кОм).
				"""
				deltaAV = instrument.read_registers(registeraddress = 30, number_of_registers = 10)
				for i in range(10):
					self._dataP1[8][i] = round((deltaAV[i] / 1000), 3)
				"""
				Плата 1 Сопротивление изоляции 1 (MОм).
				"""
				RZ1 = instrument.read_registers(registeraddress = 50, number_of_registers = 10)
				for i in range(10):
					self._dataP1[9][i] = round((RZ1[i] * 16 / 1000), 2)
				"""
				Плата 1 Сопротивление изоляции 2 (MОм).
				"""
				RZ2 = instrument.read_registers(registeraddress = 60, number_of_registers = 10)
				for i in range(10):
					self._dataP1[10][i] = round((RZ2[i] * 16 / 1000), 2)
				"""
				Плата 1 Cопротивление шлейфа (кОм).
				"""
				Rloop1 = instrument.read_registers(registeraddress = 70, number_of_registers = 10)
				for i in range(10):
					self._dataP1[11][i] = round((Rloop1[i] / 1000), 3)
				"""
				Плата 1 Значение напряжения на входе 1  В.
				"""
				Uin1 = instrument.read_registers(registeraddress = 190, number_of_registers = 10)
				self._dataP1[12] = Uin1
				"""
				Плата 1 Значение напряжения на входе 2  В.
				"""
				Uin2 = instrument.read_registers(registeraddress = 230, number_of_registers = 10)
				self._dataP1[13] = Uin2
				"""
				Плата 1 Значение объемного напряжения 1 В.
				"""
				Um = 100.0  # Напряжение измерения
				Rp1 = instrument.read_registers(registeraddress = 150, number_of_registers = 10)
				Rm1 = instrument.read_registers(registeraddress = 170, number_of_registers = 10)
				K1 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
				Ux1 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
				Rdp1 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
				Rdm1 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
				for i in range(10):
					Rdp1[i] = float(Rp1[i])
					Rdm1[i] = float(Rm1[i])
					if Rdp1[i] >= Rdm1[i]:
						K1[i] = (Rdp1[i] + 2447 / 16) / (Rdm1[i] + 2447 / 16)
						Ux1[i] = -(Um * (K1[i] - 1)) / (K1[i] + 1)
					else:
						K1[i] = (Rdm1[i] + 2447 / 16) / (Rdp1[i] + 2447 / 16)
						Ux1[i] = (Um * (K1[i] - 1)) / (K1[i] + 1)
					self._dataP1[14][i] = Ux1[i]
				# print('Rp1', Rdp1)
				# print('Rm1', Rdm1)
				"""
				Плата 1 Значение объемного напряжения 2 В.
				"""
				Um = 100.0  # Напряжение измерения
				Rp2 = instrument.read_registers(registeraddress = 160, number_of_registers = 10)
				Rm2 = instrument.read_registers(registeraddress = 180, number_of_registers = 10)
				K2 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
				Ux2 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
				Rdp2 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
				Rdm2 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
				for i in range(10):
					Rdp2[i] = float(Rp2[i])
					Rdm2[i] = float(Rm2[i])
					if Rdp2[i] >= Rdm2[i]:
						K2[i] = (Rdp2[i] + 2447 / 16) / (Rdm2[i] + 2447 / 16)
						Ux2[i] = -(Um * (K2[i] - 1)) / (K2[i] + 1)
					else:
						K2[i] = (Rdm2[i] + 2447 / 16) / (Rdp2[i] + 2447 / 16)
						Ux2[i] = (Um * (K2[i] - 1)) / (K2[i] + 1)
					self._dataP1[15][i] = Ux2[i]
				# print('Rp2', Rdp2)
				# print('Rm2', Rdm2)
				"""
				Плата 1 Значение сопротивления изоляции 1 ниже заданного диапазона (авария предупреждение)
				"""
				alarmRz1 = instrument.read_bits(registeraddress = 20, number_of_bits = 10)
				warnRz1 = instrument.read_bits(registeraddress = 110, number_of_bits = 10)
				for i in range(10):
					if alarmRz1[i] == 0:
						self._dataP1[16][i] = 2
					elif warnRz1[i] == 0:
						self._dataP1[16][i] = 1
					else:
						self._dataP1[16][i] = 0

				# print("alarm rz1", self._dataP1[14][0])
				"""
				Плата 1 Значение сопротивления изоляции 2 ниже заданного диапазона (авария предупреждение)
				"""
				alarmRz2 = instrument.read_bits(registeraddress = 30, number_of_bits = 10)
				warnRz2 = instrument.read_bits(registeraddress = 120, number_of_bits = 10)
				for i in range(10):
					if alarmRz2[i] == 0:
						self._dataP1[17][i] = 2
					elif warnRz2[i] == 0:
						self._dataP1[17][i] = 1
					else:
						self._dataP1[17][i] = 0
				"""
				Плата 1 Значение сопротивления шлейфа ниже заданного диапазона (авария предупреждение)
				"""
				alarmRloop = instrument.read_bits(registeraddress = 40, number_of_bits = 10)
				warnRloop = instrument.read_bits(registeraddress = 130, number_of_bits = 10)
				for i in range(10):
					if alarmRloop[i] == 0:
						self._dataP1[18][i] = 2
					elif warnRloop[i] == 0:
						self._dataP1[18][i] = 1
					else:
						self._dataP1[18][i] = 0
				"""
				Плата 1 Значение сопротивления шлейфа выше заданного диапазона (авария предупреждение)
				"""
				alarmRloopH = instrument.read_bits(registeraddress = 50, number_of_bits = 10)
				warnRloopH = instrument.read_bits(registeraddress = 160, number_of_bits = 10)
				for i in range(10):
					if alarmRloopH[i] == 0:
						self._dataP1[19][i] = 2
					elif warnRloopH[i] == 0:
						self._dataP1[19][i] = 1
					else:
						self._dataP1[19][i] = 0
				"""
				Плата 1 Напряжение на входе 1 выше заданного диапазона (авария )
				"""
				U1_alarm = instrument.read_bits(registeraddress = 140, number_of_bits = 10)
				self._dataP1[20] = U1_alarm
				# print("U1 =", U1_alarm)
				"""
				Плата 1 Напряжение на входе 2 выше заданного диапазона (авария )
				"""
				U2_alarm = instrument.read_bits(registeraddress = 150, number_of_bits = 10)
				self._dataP1[21] = U2_alarm
				"""
				Плата 1 Неисправность АЦП
				"""
				DAC1_alarm = instrument.read_register(registeraddress = 220)
				for i in range(10):
					self._dataP1[22][i] = byte_to_bit(DAC1_alarm, i)
				"""
				Плата 1 Неисправность +100 В
				"""
				alarmP100V = instrument.read_register(registeraddress = 222)
				for i in range(10):
					self._dataP1[23][i] = byte_to_bit(alarmP100V, i)
				"""
				Плата 1 Неисправность +100 В
				"""
				alarmM100V = instrument.read_register(registeraddress = 221)
				for i in range(10):
					self._dataP1[24][i] = byte_to_bit(alarmM100V, i)


			except IOError:
				print("нет связи с устройсвом по адресу", str(self._dataP4[0][0]))
				self._dataP4[5][0] = 1
			# 	# instrument.serial.close()
			# 	time.sleep(5)
			# 	instrument.close_port_after_each_call = True
			else:
				self._dataP4[5][0] = 0
				# Rz1 = instrument.read_registers (registeraddress = 50, number_of_registers = 10)
				# print ("DATA Line", self._dataP4[5][2])
				# print ('QWERT=', Rz1[0])

				# for i in range (10):
				# 	self._dataP1[13][i] = (Rz1[i]*16)/100
				# a = Rz1[0]

				# self._dataP1[0] = ' '
				# print ("AAAAA = ", a)
				# print ("The type of a", type (Rz1))
				# print ("The type of B", type (self._dataP1))
				# print ("Подключение по Modbus RTU выполнено")
				# print ('RZ1 = ', Rz1)

				instrument.serial.close()
			instrument.serial.close()
		# instrument.serial.close()
	def con_2(self):

		try:
			instrument = minimalmodbus.Instrument('/dev/ttyUSB0', (int(self._dataP4[0][0]+1)))
			instrument.serial.baudrate = 9600
			instrument.serial.timeout = 1.0
			instrument.mode = minimalmodbus.MODE_RTU

		# instrument.close_port_after_each_call = True
		except Exception as error:
			print ("[!] Exception occurred: ", error)
			# errorcounter = errorcounter + 1
			print("Ошибка подключения по RS-485_2 IOError ")
			# instrument.close_port_after_each_call = True
			self._dataP4[4][1] = 1 # Ошибка подключения по RS-485
			# time.sleep(5)
		# except (FileNotFoundError, IOError, RuntimeError, TypeError, NameError, IndexError):
		# 	print("Ошибка подключения по RS-485_2 - File Not Found")
		# 	instrument.close_port_after_each_call = True
		# except (IOError, RuntimeError, TypeError, NameError, UnboundLocalError, FileNotFoundError):
		# 	print("Ошибка подключения по RS-485_2 ")
		# 	instrument.close_port_after_each_call = True
		# instrument.serial.close()
		else:
			self._dataP4[4][1] = 0
			# print("Подключение по RS - 485 выполнено")
			try:
				""""
				режим ПМК
				"""
				modePmk2 = instrument.read_register(registeraddress = 145)
				self._dataP4[10][1] = modePmk2
				""""
				Номер версии ПО
				"""
				Nversion = instrument.read_registers(registeraddress = 90, number_of_registers = 2)
				self._dataP4[10][2] = (Nversion[0] * 65536 + Nversion[1])

				# print('NVERSION = ', self._dataP4[1][2])
				instrument.close_port_after_each_call = True
				""""
				ID шасси
				"""
				IDpmk2 = instrument.read_registers(registeraddress = 110, number_of_registers = 2)
				self._dataP4[10][3] = (IDpmk2[0] * 65536 + IDpmk2[1])
				""""
				ID платы измерения 1
				"""
				IDpi1 = instrument.read_registers(registeraddress = 100, number_of_registers = 6)
				self._dataP4[10][4] = IDpi1[0]
				self._dataP4[10][5] = IDpi1[1]
				self._dataP4[10][6] = IDpi1[2]
				self._dataP4[10][7] = IDpi1[3]
				self._dataP4[10][8] = IDpi1[4]
				self._dataP4[10][9] = IDpi1[5]
				"""
				Контрольная сумма ПО md5
				"""
				md5 = instrument.read_registers(registeraddress = 120, number_of_registers = 8)
				self._dataP4[12][0] = md5[0]
				self._dataP4[12][1] = md5[1]
				self._dataP4[12][2] = md5[2]
				self._dataP4[12][3] = md5[3]
				self._dataP4[12][4] = md5[4]
				self._dataP4[12][5] = md5[5]
				self._dataP4[12][6] = md5[6]
				self._dataP4[12][7] = md5[7]
				"""
				Режим старта
				"""
				modeStart2 = instrument.read_bit(registeraddress = 200)
				self._dataP4[13][0] = modeStart2
				""""
				Плата 2 режим работы канала
				"""
				modeCh2 = instrument.read_registers(registeraddress = 40, number_of_registers = 10)
				self._dataP2[0] = modeCh2
				""""
				Плата 1 Диапазон сопротивления изоляции аварийный
				"""
				deltaAV = instrument.read_registers(registeraddress = 0, number_of_registers = 10)
				for i in range(10):
					self._dataP2[1][i] = deltaAV[i] >> 8
				""""
				Плата 1 Диапазон сопротивления шлейфа аварийный
				"""
				for i in range(10):
					self._dataP2[2][i] = deltaAV[i] & 0x00FF
				""""
				Плата 1 Диапазон сопротивления изоляции предупредительный
				"""
				deltaAV = instrument.read_registers(registeraddress = 250, number_of_registers = 10)
				for i in range(10):
					self._dataP2[3][i] = deltaAV[i] >> 8
				""""
				Плата 1 Диапазон сопротивления шлейфа предупредительный
				"""
				for i in range(10):
					self._dataP2[4][i] = deltaAV[i] & 0x00FF
				""""
				Плата 1 Допустимое значение напряжения на входе В.
				"""
				deltaAV = instrument.read_registers(registeraddress = 200, number_of_registers = 10)
				self._dataP2[5] = deltaAV
				""""
				Плата 1 Уставка сопротивления изоляции 1 (MОм).
				"""
				deltaAV = instrument.read_registers(registeraddress = 10, number_of_registers = 10)
				for i in range(10):
					self._dataP2[6][i] = round((deltaAV[i] * 16 / 1000), 2)
				"""
				Плата 1 Уставка сопротивления изоляции 2 (MОм).
				"""
				deltaAV = instrument.read_registers(registeraddress = 20, number_of_registers = 10)
				for i in range(10):
					self._dataP2[7][i] = round((deltaAV[i] * 16 / 1000), 2)
				"""
				Плата 1 Уставка сопротивления шлейфа (кОм).
				"""
				deltaAV = instrument.read_registers(registeraddress = 30, number_of_registers = 10)
				for i in range(10):
					self._dataP2[8][i] = round((deltaAV[i] / 1000), 3)
				"""
				Плата 1 Сопротивление изоляции 1 (MОм).
				"""
				RZ1 = instrument.read_registers(registeraddress = 50, number_of_registers = 10)
				for i in range(10):
					self._dataP2[9][i] = round((RZ1[i] * 16 / 1000), 2)
				"""
				Плата 1 Сопротивление изоляции 2 (MОм).
				"""
				RZ1 = instrument.read_registers(registeraddress = 60, number_of_registers = 10)
				for i in range(10):
					self._dataP2[10][i] = round((RZ1[i] * 16 / 1000), 2)
				"""
				Плата 1 Cопротивление шлейфа (кОм).
				"""
				Rloop = instrument.read_registers(registeraddress = 70, number_of_registers = 10)
				for i in range(10):
					self._dataP2[11][i] = round((Rloop[i] / 1000), 3)
				"""
				Плата 1 Значение напряжения на входе 1  В.
				"""
				Uin1 = instrument.read_registers(registeraddress = 190, number_of_registers = 10)
				self._dataP2[12] = Uin1
				"""
				Плата 1 Значение напряжения на входе 2  В.
				"""
				Uin2 = instrument.read_registers(registeraddress = 230, number_of_registers = 10)
				self._dataP2[13] = Uin2
				"""
				Плата 1 Значение объемного напряжения 1 В.
				"""
				Um = 100.0  # Напряжение измерения
				Rp1 = instrument.read_registers(registeraddress = 150, number_of_registers = 10)
				Rm1 = instrument.read_registers(registeraddress = 170, number_of_registers = 10)
				K1 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
				Ux1 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
				Rdp1 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
				Rdm1 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
				for i in range(10):
					Rdp1[i] = float(Rp1[i])
					Rdm1[i] = float(Rm1[i])
					if Rdp1[i] >= Rdm1[i]:
						K1[i] = (Rdp1[i] + 2447 / 16) / (Rdm1[i] + 2447 / 16)
						Ux1[i] = -(Um * (K1[i] - 1)) / (K1[i] + 1)
					else:
						K1[i] = (Rdm1[i] + 2447 / 16) / (Rdp1[i] + 2447 / 16)
						Ux1[i] = (Um * (K1[i] - 1)) / (K1[i] + 1)
					self._dataP2[14][i] = round(Ux1[i], 2)
				# print('Rp1', Rdp1)
				# print('Rm1', Rdm1)
				"""
				Плата 1 Значение объемного напряжения 2 В.
				"""
				Um = 100.0  # Напряжение измерения
				Rp2 = instrument.read_registers(registeraddress = 160, number_of_registers = 10)
				Rm2 = instrument.read_registers(registeraddress = 180, number_of_registers = 10)
				K2 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
				Ux2 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
				Rdp2 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
				Rdm2 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
				for i in range(10):
					Rdp2[i] = float(Rp2[i])
					Rdm2[i] = float(Rm2[i])
					if Rdp2[i] >= Rdm2[i]:
						K2[i] = (Rdp2[i] + 2447 / 16) / (Rdm2[i] + 2447 / 16)
						Ux2[i] = -(Um * (K2[i] - 1)) / (K2[i] + 1)
					else:
						K2[i] = (Rdm2[i] + 2447 / 16) / (Rdp2[i] + 2447 / 16)
						Ux2[i] = (Um * (K2[i] - 1)) / (K2[i] + 1)
					self._dataP2[15][i] = round(Ux2[i], 2)

				# print('Rp2', Rdp2)
				# print('Rm2', Rdm2)
				"""
				Плата 1 Значение сопротивления изоляции 1 ниже заданного диапазона (авария предупреждение)
				"""
				alarmRz1 = instrument.read_bits(registeraddress = 20, number_of_bits = 10)
				warnRz1 = instrument.read_bits(registeraddress = 110, number_of_bits = 10)
				for i in range(10):
					if alarmRz1[i] == 0:
						self._dataP2[16][i] = 2
					elif warnRz1[i] == 0:
						self._dataP2[16][i] = 1
					else:
						self._dataP2[16][i] = 0

				# print("alarm rz1", self._dataP1[14][0])
				"""
				Плата 1 Значение сопротивления изоляции 2 ниже заданного диапазона (авария предупреждение)
				"""
				alarmRz2 = instrument.read_bits(registeraddress = 30, number_of_bits = 10)
				warnRz2 = instrument.read_bits(registeraddress = 120, number_of_bits = 10)
				for i in range(10):
					if alarmRz2[i] == 0:
						self._dataP2[17][i] = 2
					elif warnRz2[i] == 0:
						self._dataP2[17][i] = 1
					else:
						self._dataP2[17][i] = 0
				"""
				Плата 1 Значение сопротивления шлейфа ниже заданного диапазона (авария предупреждение)
				"""
				alarmRloop = instrument.read_bits(registeraddress = 40, number_of_bits = 10)
				warnRloop = instrument.read_bits(registeraddress = 130, number_of_bits = 10)
				for i in range(10):
					if alarmRloop[i] == 0:
						self._dataP2[18][i] = 2
					elif warnRloop[i] == 0:
						self._dataP2[18][i] = 1
					else:
						self._dataP2[18][i] = 0
				"""
				Плата 1 Значение сопротивления шлейфа выше заданного диапазона (авария предупреждение)
				"""
				alarmRloopH = instrument.read_bits(registeraddress = 50, number_of_bits = 10)
				warnRloopH = instrument.read_bits(registeraddress = 160, number_of_bits = 10)
				for i in range(10):
					if alarmRloopH[i] == 0:
						self._dataP2[19][i] = 2
					elif warnRloopH[i] == 0:
						self._dataP2[19][i] = 1
					else:
						self._dataP2[19][i] = 0
				"""
				Плата 1 Напряжение на входе 1 выше заданного диапазона (авария )
				"""
				U1_alarm = instrument.read_bits(registeraddress = 140, number_of_bits = 10)
				self._dataP2[20] = U1_alarm
				# print("U1 =", U1_alarm)
				"""
				Плата 1 Напряжение на входе 2 выше заданного диапазона (авария )
				"""
				U2_alarm = instrument.read_bits(registeraddress = 150, number_of_bits = 10)
				self._dataP2[21] = U2_alarm
				"""
				Плата 1 Неисправность АЦП
				"""
				DAC1_alarm = instrument.read_register(registeraddress = 220)
				for i in range(10):
					self._dataP2[22][i] = byte_to_bit(DAC1_alarm, i)
				"""
				Плата 1 Неисправность +100 В
				"""
				alarmP100V = instrument.read_register(registeraddress = 222)
				for i in range(10):
					self._dataP2[23][i] = byte_to_bit(alarmP100V, i)
				"""
				Плата 1 Неисправность +100 В
				"""
				alarmM100V = instrument.read_register(registeraddress = 221)
				for i in range(10):
					self._dataP2[24][i] = byte_to_bit(alarmM100V, i)


			except IOError:
				print("нет связи с устройсвом по адресу", str(self._dataP4[0][0]+1))
				self._dataP4[5][1] = 1
			# 	# instrument.serial.close()
			# 	time.sleep(5)
			# 	instrument.close_port_after_each_call = True
			else:
				self._dataP4[5][1] = 0
				instrument.serial.close()
			self._dataP4[14][0] = self._dataP4[4][0]
			self._dataP4[14][1] = self._dataP4[4][1]
			self._dataP4[15][0] = self._dataP4[5][0]
			self._dataP4[15][1] = self._dataP4[5][1]

			instrument.serial.close()

# region Absract Model
class PandasModel(QAbstractTableModel):
	def __init__(self, data):
		super().__init__()
		self._data = data

	# def update_data(self, data):
	#         #changes data in column 1 and 3
	#         #data updates 10x per second
	#         self.beginResetModel()
	#         self.data = data
	#         self.endResetModel()

	def rowCount(self, index):
		return self._data.shape[0]

	def columnCount(self, index):
		return self._data.shape[1]

	def data(self, index, role = Qt.DisplayRole):
		if index.isValid():
			if role == Qt.DisplayRole or role == Qt.EditRole:
				value = self._data.iloc[index.row(), index.column()]
				return str(value)
			if role == Qt.BackgroundRole and index.row() == 0:
				# See below for the data structure.
				return QtGui.QColor('blue')
		if role == Qt.TextAlignmentRole:
			value = self._data.iloc[index.row()][index.column()]

			if isinstance(value, int) or isinstance(value, float) or isinstance(value, double):
				# Align right, vertical middle.
				return Qt.AlignVCenter + Qt.AlignRight

	def setData(self, index, value, role):
		if role == Qt.EditRole:
			try:
				value = int(value)
			except ValueError:
				return False
			self._data.iloc[index.row(), index.column()] = value
			return True
		return False

	def flags(self, index):
		return Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable

	def headerData(self, section, orientation, role):
		# section is the index of the column/row.
		if role == Qt.DisplayRole:
			if orientation == Qt.Horizontal:
				return str(self._data.columns[section])

			if orientation == Qt.Vertical:
				return str(self._data.index[section])


# endregion
# region MainWindow
class MainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self):
		super().__init__()
		Ui_MainWindow.__init__(self)
		self.setupUi(self)
		self.Button_con.clicked.connect(self.defAddMb)

		self.table = QTableView()
		self.timer = QTimer(self)
		self.timer.timeout.connect(self.update_table)
		# self.tableView_Arhive.setModel ( self.model )
		# self.timer.timeout(self.update_table)
		self.timer.start(60 * 10)

		self._dataP1 = None
		self._dataP2 = None
		self._dataP3 = None
		self._dataP4 = None

		self._counter1 = 0
		self._counter2 = 0
		self._counter3 = 0
		self._counter4 = 0
		self._delay1 = 2
		self._delay2 = 10

	def update_table(self):
		self._dataP1 = dataP1
		self._dataP2 = dataP2
		self._dataP4 = dataP4
		# self.model1 = PandasModel(dataP3)
		# self.model1.dataChanged.emit(QtCore.QModelIndex(), QtCore.QModelIndex())
		# self.tableView_Arhive.setModel(self.model1)
		# self.model1.dataChanged.emit(QtCore.QModelIndex(), QtCore.QModelIndex())
		# self.beginResetModel()

		"""
		Состояние сети 
		"""
		RS1 = (int(dataP4[4][0]) == 1)
		RS2 = (int(dataP4[4][1]) == 1)
		ID1 = (int(dataP4[5][0]) == 1)
		ID2 = (int(dataP4[5][1]) == 1)
		if (RS1 | RS2) == 1:
			if (self._counter1 < self._delay1):
				self._counter1 += 1
			else:
				self.label_info.setText('Нет подключения по RS-485')
				self.label_info.setStyleSheet('font-weight: bold; color: black')
				self.label_info.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
		else:
			self._counter1 = 0

		if ((ID1 & ID2) == 1) & ((RS1 | RS2) == 0) == 1:
			if (self._counter2 < self._delay2):
				self._counter2 += 1
			else:
				numID1 = int(self._dataP4[0][0])
				numID1 = str(hex(numID1))
				numID2 = int(self._dataP4[0][0]) + 1
				numID2 = str(hex(numID2))
				self.label_info.setText("Нет связи с устройсвами по адресу " + numID1 + ' и ' + numID2)
				self.label_info.setStyleSheet('font-weight: bold; color: red')
				self.label_info.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
		else:
			self._counter2 = 0

		if ID1 & (not ID2) & ((RS1 | RS2) == 0) == 1:
			if (self._counter3 < self._delay2):
				self._counter3 += 1
			else:
				numID1 = int(self._dataP4[0][0])
				numID1 = str(hex(numID1))
				self.label_info.setText("Нет связи с устройсвами по адресу " + numID1)
				self.label_info.setStyleSheet('font-weight: bold; color: red')
				self.label_info.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
		else:
			self._counter3 = 0

		if ID2 & (not ID1) & ((RS1 | RS2) == 0) == 1:
			if (self._counter4 < self._delay2):
				self._counter4 += 1
			else:
				numID2 = int(self._dataP4[0][0]) + 1
				numID2 = str(hex(numID2))
				self.label_info.setText("Нет связи с устройсвами по адресу " + numID2)
				self.label_info.setStyleSheet('font-weight: bold; color: red')
				self.label_info.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
		else:
			self._counter4 = 0

		if ((not RS1) & (not RS2) & (not ID1) & (not ID2)) == 1:  # ((dataP4[4][0] == 0) | (dataP4[4][1] == 0))
			self.label_info.setText('Подключение по RS-485 выполнено')
			self.label_info.setStyleSheet('font-weight: bold; color: black')
			self.label_info.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)

		"""
		TableWidgt Окно ПМК20 1
		"""
		# dataP4[4][0] = 0 #self._dataP4[4][0]

		if (dataP4[5][0] == 0):
			# self.tableWidget.setItem(2, 0, QTableWidgetItem(str(int(dataP4[0][0]))))
			var = int(dataP4[1][1])
			if var == 0:
				msg = 'Пауза перед измерением наряжения (Р-0)'
			elif var == 1:
				msg = 'Измерение напряжения (Р-1)'
			elif var == 2:
				msg = 'Пауза перед подачей напряжения U = -100 V (Р-2)'
			elif var == 3:
				msg = 'Пауза после подачи напряжения U = -100 V (Р-3)'
			elif var == 4:
				msg = 'Измерение сопротивления при U = -100 V (Р-4)'
			elif var == 5:
				msg = 'Пауза после измерения сопротивления U = -100 V (Р-5)'
			elif var == 6:
				msg = 'Пауза после снятия нпряжения U = -100 V (Р-6)'
			elif var == 7:
				msg = 'Пауза после подачи напряжения U = +100 V (Р-7)'
			elif var == 8:
				msg = 'Измерение сопротивления при U = +100 V (Р-8)'
			elif var == 9:
				msg = 'Пауза после измерения сопротивления U = +100 V (Р-9)'
			else:
				msg = 'Пауза после снятия напряжения U = +100 V (Р-10)'

			self.tableWidget_PMK.setItem(0, 0, QTableWidgetItem(msg))  # режим ПМК
			numVersion = str(int(dataP4[1][2]))
			self.tableWidget_PMK.setItem(1, 0, QTableWidgetItem(numVersion))  # Номер версии
			idPMK1 = int(dataP4[1][3])
			idPMK1 = str(hex(idPMK1))

			self.tableWidget_PMK.setItem(2, 0, QTableWidgetItem(idPMK1))  # Номер шасси ПМК

			md5 = (str(hex(int(dataP4[2][0]))) + ' ' + str(hex(int(dataP4[2][1]))) + ' ' + str(
				hex(int(dataP4[2][2]))) + ' ' + str(hex(int(dataP4[2][3]))) + ' ' + str(
				hex(int(dataP4[2][4]))) + ' ' + str(hex(int(dataP4[2][5]))) + ' ' + str(
				hex(int(dataP4[2][6]))) + ' ' + str(hex(int(dataP4[2][7]))))
			self.tableWidget_PMK.setItem(5, 0, QTableWidgetItem(md5))  # md5
			idPi1 = (str(hex(int(dataP4[1][4]))) + ' ' + str(hex(int(dataP4[1][5]))) + ' ' + str(
				hex(int(dataP4[1][6]))) + ' ' + str(hex(int(dataP4[1][7]))) + ' ' + str(
				hex(int(dataP4[1][8]))) + ' ' + str(hex(int(dataP4[1][9]))))
			self.tableWidget_PMK.setItem(3, 0, QTableWidgetItem(idPi1))  # Номер платы измерения 2
		else:
			self.tableWidget_PMK.setItem(3, 0, QTableWidgetItem('Н/Д'))  # блокировка  значения по RS устр - во
			self.tableWidget_PMK.item(3, 0).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
			self.tableWidget_PMK.item(3, 0).setBackground(QtGui.QColor(208, 210,
				177))  # серый  # self.tableWidget_PMK.item(3, 0).setForeground(QtGui.QColor(0, 0, 0))

		if (dataP4[5][1] == 0):
			self.tableWidget_PMK.setItem(2, 0, QTableWidgetItem(str(int(dataP4[0][0]))))
			var = int(dataP4[10][1])
			if var == 0:
				msg = 'Пауза перед измерением наряжения (Р-0)'
			elif var == 1:
				msg = 'Измерение напряжения (Р-1)'
			elif var == 2:
				msg = 'Пауза перед подачей напряжения U = -100 V (Р-2)'
			elif var == 3:
				msg = 'Пауза после подачи напряжения U = -100 V (Р-3)'
			elif var == 4:
				msg = 'Измерение сопротивления при U = -100 V (Р-4)'
			elif var == 5:
				msg = 'Пауза после измерения сопротивления U = -100 V (Р-5)'
			elif var == 6:
				msg = 'Пауза после снятия нпряжения U = -100 V (Р-6)'
			elif var == 7:
				msg = 'Пауза после подачи напряжения U = +100 V (Р-7)'
			elif var == 8:
				msg = 'Измерение сопротивления при U = +100 V (Р-8)'
			elif var == 9:
				msg = 'Пауза после измерения сопротивления U = +100 V (Р-9)'
			else:
				msg = 'Пауза после снятия напряжения U = +100 V (Р-10)'

			self.tableWidget_PMK.setItem(0, 0, QTableWidgetItem(msg))  # режим ПМК
			numVersion = str(int(dataP4[10][2]))
			self.tableWidget_PMK.setItem(1, 0, QTableWidgetItem(numVersion))  # Номер версии
			idPMK2 = int(dataP4[10][3])
			idPMK2 = str(hex(idPMK2))

			self.tableWidget_PMK.setItem(2, 0, QTableWidgetItem(idPMK2))  # Номер шасси ПМК

			md5 = (str(hex(int(dataP4[12][0]))) + ' ' + str(hex(int(dataP4[2][1]))) + ' ' + str(
				hex(int(dataP4[12][2]))) + ' ' + str(hex(int(dataP4[2][3]))) + ' ' + str(
				hex(int(dataP4[2][4]))) + ' ' + str(hex(int(dataP4[12][5]))) + ' ' + str(
				hex(int(dataP4[2][6]))) + ' ' + str(hex(int(dataP4[2][7]))))
			self.tableWidget_PMK.setItem(5, 0, QTableWidgetItem(md5))  # md5

			idPi2 = (str(hex(int(dataP4[10][4]))) + ' ' + str(hex(int(dataP4[10][5]))) + ' ' + str(
				hex(int(dataP4[10][6]))) + ' ' + str(hex(int(dataP4[10][7]))) + ' ' + str(
				hex(int(dataP4[10][8]))) + ' ' + str(hex(int(dataP4[10][9]))))
			self.tableWidget_PMK.setItem(4, 0, QTableWidgetItem(idPi2))  # Номер платы измерения 1
		else:
			self.tableWidget_PMK.setItem(4, 0, QTableWidgetItem('Н/Д'))  # б
			self.tableWidget_PMK.item(4, 0).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
			self.tableWidget_PMK.item(4, 0).setBackground(QtGui.QColor(208, 210, 177))  # серый
			self.tableWidget_PMK.item(4, 0).setForeground(QtGui.QColor(0, 0, 0))

			for k in [1, 3, 4, 5, 6, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 21, 22, 23, 24, 25, 26]:
				for i in range(10):
					self.tblitems_2.setItem(k, i, QTableWidgetItem('Н/Д'))  # блокировка  значения по RS плата 1
					self.tblitems_2.item(k, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
					self.tblitems_2.item(k, i).setBackground(QtGui.QColor(208, 210, 177))  # серый
					self.tblitems_2.item(k, i, ).setForeground(QtGui.QColor(0, 0, 0))

		"""
		tblitems_1 окно Плата 1
		"""
		for i in range(10):
			modeCh1 = int(dataP1[0][i])  # режим работы канала платы 1
			modeStart1 = int(dataP4[3][0])
			block_start1 = 0
			if modeStart1 == 0:
				self.tblitems_1.setItem(1, i, QTableWidgetItem('ОТКЛ.'))
				self.tblitems_1.item(1, i).setBackground(QtGui.QColor(0, 0, 255))  # Зеленый
				self.tblitems_1.item(1, i, ).setForeground(QtGui.QColor(255, 255, 255))
				self.tblitems_1.item(1, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
				block_start1 = 1  # блокировка отображения в момент старта
			elif ((modeCh1 == 0) | (modeCh1 == 1) | (modeCh1 == 3) | (modeCh1 == 4) | (modeCh1 == 5)):
				block_start1 = 0
				self.tblitems_1.setItem(1, i, QTableWidgetItem('ОТКЛ.'))
				self.tblitems_1.item(1, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
			elif modeCh1 == 9:
				self.tblitems_1.setItem(1, i, QTableWidgetItem('ОТКЛ.'))
				self.tblitems_1.item(1, i).setBackground(QtGui.QColor(0, 0, 255))  # Синий
				self.tblitems_1.item(1, i, ).setForeground(QtGui.QColor(255, 255, 255))
				self.tblitems_1.item(1, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
			else:
				block_start1 = 0
				self.tblitems_1.setItem(1, i, QTableWidgetItem('ВКЛ.'))
				self.tblitems_1.item(1, i).setBackground(QtGui.QColor(0, 255, 0))  # Зеленый
				self.tblitems_1.item(1, i, ).setForeground(QtGui.QColor(0, 0, 0))
				self.tblitems_1.item(1, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
		for i in range(10):
			deltaAlarm1ch = str(int(dataP1[1][i])) + ' %'
			self.tblitems_1.setItem(3, i,
				QTableWidgetItem(deltaAlarm1ch))  # допустимое авар. отклонение сопр. изоляции 1
			self.tblitems_1.item(3, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
		for i in range(10):
			deltaAlarm1ch = str(int(dataP1[2][i])) + ' %'
			self.tblitems_1.setItem(4, i,
				QTableWidgetItem(deltaAlarm1ch))  # допустимое авар. отклонение сопр. шлеййфа 1
			self.tblitems_1.item(4, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
		for i in range(10):
			deltaWorn1ch = str(int(dataP1[3][i])) + ' %'
			self.tblitems_1.setItem(5, i,
				QTableWidgetItem(deltaWorn1ch))  # допустимое прдедупр. отклонение сопр. изоляции 1
			self.tblitems_1.item(5, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
		for i in range(10):
			deltaWorn1ch = str(int(dataP1[4][i])) + ' %'
			self.tblitems_1.setItem(6, i,
				QTableWidgetItem(deltaWorn1ch))  # допустимое предупр. отклонение сопр. шлеййфа 1
			self.tblitems_1.item(6, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
		for i in range(10):
			setUch1 = str(int(dataP1[5][i]))  # +' В'
			self.tblitems_1.setItem(8, i, QTableWidgetItem(setUch1))  # допустимое значение напряжения на входе
			self.tblitems_1.item(8, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
		for i in range(10):
			setRZ1 = str(dataP1[6][i])  # +' MОм'
			self.tblitems_1.setItem(9, i, QTableWidgetItem(setRZ1))  # уставка сопр. изоляции 1
			self.tblitems_1.item(9, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
		for i in range(10):
			setRZ2 = str(dataP1[7][i])  # + ' MОм'
			self.tblitems_1.setItem(10, i, QTableWidgetItem(setRZ2))  # уставка сопр. изоляции 2
			self.tblitems_1.item(10, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
		for i in range(10):
			setRloop = str(dataP1[8][i])  # + ' кОм'
			self.tblitems_1.setItem(11, i, QTableWidgetItem(setRloop))  # уставка сопр. шлеййфа
			self.tblitems_1.item(11, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
		for i in range(10):
			RZ1 = str(dataP1[9][i])  # +' MОм'
			self.tblitems_1.setItem(13, i, QTableWidgetItem(RZ1))  # Cопр. изоляции 1
			self.tblitems_1.item(13, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
		for i in range(10):
			RZ2 = str(dataP1[10][i])  # +' MОм'
			self.tblitems_1.setItem(14, i, QTableWidgetItem(RZ2))  # Cопр. изоляции 2
			self.tblitems_1.item(14, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
		for i in range(10):
			Rloop = str(dataP1[11][i])  # + ' кОм'
			self.tblitems_1.setItem(15, i, QTableWidgetItem(Rloop))  # Сопр. шлеййфа
			self.tblitems_1.item(15, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
		for i in range(10):
			Uin1 = str(dataP1[12][i]/10)  # +' В'
			self.tblitems_1.setItem(16, i, QTableWidgetItem(Uin1))  # значение напряжения на входе1
			self.tblitems_1.item(16, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
		for i in range(10):
			Uin2 = str(dataP1[13][i]/10) # +' В'
			self.tblitems_1.setItem(17, i, QTableWidgetItem(Uin2))  # значение напряжения на входе1
			self.tblitems_1.item(17, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
		for i in range(10):
			Ux1 = str(int(dataP1[14][i]))  # +' В'
			self.tblitems_1.setItem(18, i, QTableWidgetItem(Ux1))  # значение объемного напряжения на входе1
			self.tblitems_1.item(18, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
		for i in range(10):
			Ux2 = str(int(dataP1[15][i]))  # +' В'
			self.tblitems_1.setItem(19, i, QTableWidgetItem(Ux2))  # значение объемного напряжения на входе1
			self.tblitems_1.item(19, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
		for i in range(10):
			AlarmRz1 = int(dataP1[16][i])
			if AlarmRz1 == 2:
				self.tblitems_1.setItem(21, i, QTableWidgetItem('AВАРИЯ'))  # Авария - предупреждение сопр. изол. 1
				self.tblitems_1.item(21, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
				self.tblitems_1.item(21, i).setBackground(QtGui.QColor(255, 0, 0))  # Красный
				self.tblitems_1.item(21, i, ).setForeground(QtGui.QColor(255, 255, 255))
			elif AlarmRz1 == 1:
				self.tblitems_1.setItem(21, i, QTableWidgetItem('ПРЕДУП.'))
				self.tblitems_1.item(21, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
				self.tblitems_1.item(21, i).setBackground(QtGui.QColor(255, 255, 0))  # желтый
			else:
				self.tblitems_1.setItem(21, i, QTableWidgetItem('Норма'))
				self.tblitems_1.item(21, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
		for i in range(10):
			AlarmRz2 = int(dataP1[17][i])
			if AlarmRz2 == 2:
				self.tblitems_1.setItem(22, i, QTableWidgetItem('AВАРИЯ'))  # # Авария - предупреждение сопр. изол. 2
				self.tblitems_1.item(22, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
				self.tblitems_1.item(22, i).setBackground(QtGui.QColor(255, 0, 0))  # Красный
				self.tblitems_1.item(22, i, ).setForeground(QtGui.QColor(255, 255, 255))
			elif AlarmRz2 == 1:
				self.tblitems_1.setItem(22, i, QTableWidgetItem('ПРЕДУП.'))
				self.tblitems_1.item(22, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
				self.tblitems_1.item(22, i).setBackground(QtGui.QColor(255, 255, 0))  # желтый
			else:
				self.tblitems_1.setItem(22, i, QTableWidgetItem('Норма'))
				self.tblitems_1.item(22, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
		for i in range(10):
			AlarmRloop = int(dataP1[18][i])
			if AlarmRloop == 2:
				self.tblitems_1.setItem(23, i, QTableWidgetItem('AВАРИЯ'))  # # Авария - предупреждение сопр. шлейфа
				self.tblitems_1.item(23, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
				self.tblitems_1.item(23, i).setBackground(QtGui.QColor(255, 0, 0))  # Красный
				self.tblitems_1.item(23, i, ).setForeground(QtGui.QColor(255, 255, 255))
			elif AlarmRloop == 1:
				self.tblitems_1.setItem(23, i, QTableWidgetItem('ПРЕДУП.'))
				self.tblitems_1.item(23, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
				self.tblitems_1.item(23, i).setBackground(QtGui.QColor(255, 255, 0))  # желтый
			else:
				self.tblitems_1.setItem(23, i, QTableWidgetItem('Норма'))
				self.tblitems_1.item(23, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
		for i in range(10):
			AlarmRloopH = int(dataP1[19][i])
			if AlarmRloopH == 2:
				self.tblitems_1.setItem(24, i, QTableWidgetItem('AВАРИЯ'))  # # Авария - предупреждение сопр. шлейфа
				self.tblitems_1.item(24, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
				self.tblitems_1.item(24, i).setBackground(QtGui.QColor(255, 0, 0))  # Красный
				self.tblitems_1.item(24, i, ).setForeground(QtGui.QColor(255, 255, 255))
			elif AlarmRloopH == 1:
				self.tblitems_1.setItem(24, i, QTableWidgetItem('ПРЕДУП.'))
				self.tblitems_1.item(24, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
				self.tblitems_1.item(24, i).setBackground(QtGui.QColor(255, 255, 0))  # желтый
			else:
				self.tblitems_1.setItem(24, i, QTableWidgetItem('Норма'))
				self.tblitems_1.item(24, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
		for i in range(10):
			AlarmU1 = int(dataP1[20][i])
			if AlarmU1 == 0:
				self.tblitems_1.setItem(25, i, QTableWidgetItem('AВАРИЯ'))  # # Авария - предупреждение сопр. шлейфа
				self.tblitems_1.item(25, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
				self.tblitems_1.item(25, i).setBackground(QtGui.QColor(255, 0, 0))  # Красный
				self.tblitems_1.item(25, i, ).setForeground(QtGui.QColor(255, 255, 255))
			else:
				self.tblitems_1.setItem(25, i, QTableWidgetItem('Норма'))
				self.tblitems_1.item(25, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
		for i in range(10):
			AlarmU2 = int(dataP1[21][i])
			if AlarmU2 == 0:
				self.tblitems_1.setItem(26, i, QTableWidgetItem('AВАРИЯ'))  # # Авария - предупреждение сопр. шлейфа
				self.tblitems_1.item(26, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
				self.tblitems_1.item(26, i).setBackground(QtGui.QColor(255, 0, 0))  # Красный
				self.tblitems_1.item(26, i, ).setForeground(QtGui.QColor(255, 255, 255))
			else:
				self.tblitems_1.setItem(26, i, QTableWidgetItem('Норма'))
				self.tblitems_1.item(26, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
		for i in range(10):
			alarmDAC1 = dataP1[22][i]
			if (alarmDAC1 == 1):
				self.tblitems_d.setItem(1, i, QTableWidgetItem('AВАРИЯ'))  # # Авария - предупреждение сопр. шлейфа
				self.tblitems_d.item(1, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
				self.tblitems_d.item(1, i).setBackground(QtGui.QColor(255, 0, 0))  # Красный
				self.tblitems_d.item(1, i, ).setForeground(QtGui.QColor(255, 255, 255))
			else:
				self.tblitems_d.setItem(1, i, QTableWidgetItem('Норма'))
				self.tblitems_d.item(1, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
		for i in range(10):
			alarmP100V = dataP1[23][i]
			if (alarmP100V == 1):
				self.tblitems_d.setItem(2, i, QTableWidgetItem('AВАРИЯ'))  # # Авария - предупреждение сопр. шлейфа
				self.tblitems_d.item(2, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
				self.tblitems_d.item(2, i).setBackground(QtGui.QColor(255, 0, 0))  # Красный
				self.tblitems_d.item(2, i, ).setForeground(QtGui.QColor(255, 255, 255))
			else:
				self.tblitems_d.setItem(2, i, QTableWidgetItem('Норма'))
				self.tblitems_d.item(2, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
		for i in range(10):
			alarmP100V = dataP1[24][i]
			if (alarmP100V == 1):
				self.tblitems_d.setItem(3, i, QTableWidgetItem('AВАРИЯ'))  # # Авария - предупреждение сопр. шлейфа
				self.tblitems_d.item(3, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
				self.tblitems_d.item(3, i).setBackground(QtGui.QColor(255, 0, 0))  # Красный
				self.tblitems_d.item(3, i, ).setForeground(QtGui.QColor(255, 255, 255))
			else:
				self.tblitems_d.setItem(3, i, QTableWidgetItem('Норма'))
				self.tblitems_d.item(3, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)

		"""
		tblitems_2 окно Плата 2
		"""
		# self.label_test.setText('4.3.0 = ' + str(dataP4[3][0]) + '   ' + '4.13.0 = ' + str(dataP4[13][0]))

		for i in range(10):
			modeCh2 = int(dataP2[0][i])  # режим работы канала платы 1
			modeStart2 = int(dataP4[13][0])
			block_start2 = 0
			if modeStart2 == 0:
				self.tblitems_2.setItem(1, i, QTableWidgetItem('ОТКЛ.'))
				self.tblitems_2.item(1, i).setBackground(QtGui.QColor(0, 0, 255))  # Синий
				self.tblitems_2.item(1, i, ).setForeground(QtGui.QColor(255, 255, 255))
				self.tblitems_2.item(1, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
				block_start2 = 1  # блокировка отображения в момент старта
			elif ((modeCh2 == 0) | (modeCh2 == 1) | (modeCh2 == 3) | (modeCh2 == 4) | (modeCh2 == 5)):
				block_start2 = 0
				self.tblitems_2.setItem(1, i, QTableWidgetItem('ОТКЛ.'))
				self.tblitems_2.item(1, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
			elif modeCh2 == 9:
				self.tblitems_2.setItem(1, i, QTableWidgetItem('ОТКЛ.'))
				self.tblitems_2.item(1, i).setBackground(QtGui.QColor(0, 0, 255))  # Синий
				self.tblitems_2.item(1, i, ).setForeground(QtGui.QColor(255, 255, 255))
				self.tblitems_2.item(1, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
			else:
				block_start2 = 0
				self.tblitems_2.setItem(1, i, QTableWidgetItem('ВКЛ.'))
				self.tblitems_2.item(1, i).setBackground(QtGui.QColor(0, 255, 0))  # Зеленый
				self.tblitems_2.item(1, i, ).setForeground(QtGui.QColor(0, 0, 0))
				self.tblitems_2.item(1, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
		for i in range(10):
			deltaAlarm1ch = str(int(dataP2[1][i])) + ' %'
			self.tblitems_2.setItem(3, i,
				QTableWidgetItem(deltaAlarm1ch))  # допустимое авар. отклонение сопр. изоляции 1
			self.tblitems_2.item(3, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
		for i in range(10):
			deltaAlarm1ch = str(int(dataP2[2][i])) + ' %'
			self.tblitems_2.setItem(4, i,
				QTableWidgetItem(deltaAlarm1ch))  # допустимое авар. отклонение сопр. шлеййфа 1
			self.tblitems_2.item(4, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
		for i in range(10):
			deltaWorn1ch = str(int(dataP2[3][i])) + ' %'
			self.tblitems_2.setItem(5, i,
				QTableWidgetItem(deltaWorn1ch))  # допустимое прдедупр. отклонение сопр. изоляции 1
			self.tblitems_2.item(5, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
		for i in range(10):
			deltaWorn1ch = str(int(dataP2[4][i])) + ' %'
			self.tblitems_2.setItem(6, i,
				QTableWidgetItem(deltaWorn1ch))  # допустимое предупр. отклонение сопр. шлеййфа 1
			self.tblitems_2.item(6, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
		for i in range(10):
			setUch1 = str(int(dataP2[5][i]))  # +' В'
			self.tblitems_2.setItem(8, i, QTableWidgetItem(setUch1))  # допустимое значение напряжения на входе
			self.tblitems_2.item(8, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
		for i in range(10):
			setRZ1 = str(dataP2[6][i])  # +' MОм'
			self.tblitems_2.setItem(9, i, QTableWidgetItem(setRZ1))  # уставка сопр. изоляции 1
			self.tblitems_2.item(9, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
		for i in range(10):
			setRZ2 = str(dataP2[7][i])  # + ' MОм'
			self.tblitems_2.setItem(10, i, QTableWidgetItem(setRZ2))  # уставка сопр. изоляции 2
			self.tblitems_2.item(10, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
		for i in range(10):
			setRloop = str(dataP2[8][i])  # + ' кОм'
			self.tblitems_2.setItem(11, i, QTableWidgetItem(setRloop))  # уставка сопр. шлеййфа
			self.tblitems_2.item(11, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
		for i in range(10):
			RZ1 = str(dataP2[9][i])  # +' MОм'
			self.tblitems_2.setItem(13, i, QTableWidgetItem(RZ1))  # Cопр. изоляции 1
			self.tblitems_2.item(13, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
		for i in range(10):
			RZ2 = str(dataP2[10][i])  # +' MОм'
			self.tblitems_2.setItem(14, i, QTableWidgetItem(RZ2))  # Cопр. изоляции 2
			self.tblitems_2.item(14, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
		for i in range(10):
			Rloop = str(dataP2[11][i])  # + ' кОм'
			self.tblitems_2.setItem(15, i, QTableWidgetItem(Rloop))  # Сопр. шлеййфа
			self.tblitems_2.item(15, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
		for i in range(10):
			Uin1 = str(dataP2[12][i]/10)  # +' В'
			self.tblitems_2.setItem(16, i, QTableWidgetItem(Uin1))  # значение напряжения на входе1
			self.tblitems_2.item(16, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
		for i in range(10):
			Uin2 = str(dataP2[13][i]/10)  # +' В'
			self.tblitems_2.setItem(17, i, QTableWidgetItem(Uin2))  # значение напряжения на входе1
			self.tblitems_2.item(17, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
		for i in range(10):
			Ux1 = str(int(dataP2[14][i]))  # +' В'
			self.tblitems_2.setItem(18, i, QTableWidgetItem(Ux1))  # значение объемного напряжения на входе1
			self.tblitems_2.item(18, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
		for i in range(10):
			Ux2 = str(int(dataP2[15][i]))  # +' В'
			self.tblitems_2.setItem(19, i, QTableWidgetItem(Ux2))  # значение объемного напряжения на входе1
			self.tblitems_2.item(19, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
		for i in range(10):
			AlarmRz1 = int(dataP2[16][i])
			if AlarmRz1 == 2:
				self.tblitems_2.setItem(21, i, QTableWidgetItem('AВАРИЯ'))  # Авария - предупреждение сопр. изол. 1
				self.tblitems_2.item(21, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
				self.tblitems_2.item(21, i).setBackground(QtGui.QColor(255, 0, 0))  # Красный
				self.tblitems_2.item(21, i, ).setForeground(QtGui.QColor(255, 255, 255))
			elif AlarmRz1 == 1:
				self.tblitems_2.setItem(21, i, QTableWidgetItem('ПРЕДУП.'))
				self.tblitems_2.item(21, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
				self.tblitems_2.item(21, i).setBackground(QtGui.QColor(255, 255, 0))  # желтый
			else:
				self.tblitems_2.setItem(21, i, QTableWidgetItem('Норма'))
				self.tblitems_2.item(21, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
		for i in range(10):
			AlarmRz2 = int(dataP2[17][i])
			if AlarmRz2 == 2:
				self.tblitems_2.setItem(22, i, QTableWidgetItem('AВАРИЯ'))  # # Авария - предупреждение сопр. изол. 2
				self.tblitems_2.item(22, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
				self.tblitems_2.item(22, i).setBackground(QtGui.QColor(255, 0, 0))  # Красный
				self.tblitems_2.item(22, i, ).setForeground(QtGui.QColor(255, 255, 255))
			elif AlarmRz2 == 1:
				self.tblitems_2.setItem(22, i, QTableWidgetItem('ПРЕДУП.'))
				self.tblitems_2.item(22, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
				self.tblitems_2.item(22, i).setBackground(QtGui.QColor(255, 255, 0))  # желтый
			else:
				self.tblitems_2.setItem(22, i, QTableWidgetItem('Норма'))
				self.tblitems_2.item(22, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
		for i in range(10):
			AlarmRloop = int(dataP2[18][i])
			if AlarmRloop == 2:
				self.tblitems_2.setItem(23, i, QTableWidgetItem('AВАРИЯ'))  # # Авария - предупреждение сопр. шлейфа
				self.tblitems_2.item(23, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
				self.tblitems_2.item(23, i).setBackground(QtGui.QColor(255, 0, 0))  # Красный
				self.tblitems_2.item(23, i, ).setForeground(QtGui.QColor(255, 255, 255))
			elif AlarmRloop == 1:
				self.tblitems_2.setItem(23, i, QTableWidgetItem('ПРЕДУП.'))
				self.tblitems_2.item(23, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
				self.tblitems_2.item(23, i).setBackground(QtGui.QColor(255, 255, 0))  # желтый
			else:
				self.tblitems_2.setItem(23, i, QTableWidgetItem('Норма'))
				self.tblitems_2.item(23, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
		for i in range(10):
			AlarmRloopH = int(dataP2[19][i])
			if AlarmRloopH == 2:
				self.tblitems_2.setItem(24, i, QTableWidgetItem('AВАРИЯ'))  # # Авария - предупреждение сопр. шлейфа
				self.tblitems_2.item(24, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
				self.tblitems_2.item(24, i).setBackground(QtGui.QColor(255, 0, 0))  # Красный
				self.tblitems_2.item(24, i, ).setForeground(QtGui.QColor(255, 255, 255))
			elif AlarmRloopH == 1:
				self.tblitems_2.setItem(24, i, QTableWidgetItem('ПРЕДУП.'))
				self.tblitems_2.item(24, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
				self.tblitems_2.item(24, i).setBackground(QtGui.QColor(255, 255, 0))  # желтый
			else:
				self.tblitems_2.setItem(24, i, QTableWidgetItem('Норма'))
				self.tblitems_2.item(24, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
		for i in range(10):
			AlarmU1 = int(dataP2[20][i])
			if AlarmU1 == 0:
				self.tblitems_2.setItem(25, i, QTableWidgetItem('AВАРИЯ'))  # # Авария - предупреждение сопр. шлейфа
				self.tblitems_2.item(25, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
				self.tblitems_2.item(25, i).setBackground(QtGui.QColor(255, 0, 0))  # Красный
				self.tblitems_2.item(25, i, ).setForeground(QtGui.QColor(255, 255, 255))
			else:
				self.tblitems_2.setItem(25, i, QTableWidgetItem('Норма'))
				self.tblitems_2.item(25, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
		for i in range(10):
			AlarmU2 = int(dataP2[21][i])
			if AlarmU2 == 0:
				self.tblitems_2.setItem(26, i, QTableWidgetItem('AВАРИЯ'))  # # Авария - предупреждение сопр. шлейфа
				self.tblitems_2.item(26, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
				self.tblitems_2.item(26, i).setBackground(QtGui.QColor(255, 0, 0))  # Красный
				self.tblitems_2.item(26, i, ).setForeground(QtGui.QColor(255, 255, 255))
			else:
				self.tblitems_2.setItem(26, i, QTableWidgetItem('Норма'))
				self.tblitems_2.item(26, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
		for i in range(10):
			alarmDAC1 = dataP2[22][i]
			if (alarmDAC1 == 1):
				self.tblitems_d.setItem(5, i, QTableWidgetItem('AВАРИЯ'))  # # Авария - предупреждение сопр. шлейфа
				self.tblitems_d.item(5, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
				self.tblitems_d.item(5, i).setBackground(QtGui.QColor(255, 0, 0))  # Красный
				self.tblitems_d.item(5, i, ).setForeground(QtGui.QColor(255, 255, 255))
			else:
				self.tblitems_d.setItem(5, i, QTableWidgetItem('Норма'))
				self.tblitems_d.item(5, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
		for i in range(10):
			alarmP100V = dataP2[23][i]
			if (alarmP100V == 1):
				self.tblitems_d.setItem(6, i, QTableWidgetItem('AВАРИЯ'))  # # Авария - предупреждение сопр. шлейфа
				self.tblitems_d.item(6, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
				self.tblitems_d.item(6, i).setBackground(QtGui.QColor(255, 0, 0))  # Красный
				self.tblitems_d.item(6, i, ).setForeground(QtGui.QColor(255, 255, 255))
			else:
				self.tblitems_d.setItem(6, i, QTableWidgetItem('Норма'))
				self.tblitems_d.item(6, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
		for i in range(10):
			alarmP100V = dataP2[24][i]
			if (alarmP100V == 1):
				self.tblitems_d.setItem(7, i, QTableWidgetItem('AВАРИЯ'))  # # Авария - предупреждение сопр. шлейфа
				self.tblitems_d.item(7, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
				self.tblitems_d.item(7, i).setBackground(QtGui.QColor(255, 0, 0))  # Красный
				self.tblitems_d.item(7, i, ).setForeground(QtGui.QColor(255, 255, 255))
			else:
				self.tblitems_d.setItem(7, i, QTableWidgetItem('Норма'))
				self.tblitems_d.item(7, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
		"""
		Блокировка отображения 1
		"""
		for i in range(10):
			modeCh1 = int(dataP1[0][i])
			if modeCh1 == 9:
				for k in [13, 14, 15, 16, 17, 18, 19, 21, 22, 23, 24, 25, 26]:
					self.tblitems_1.setItem(k, i, QTableWidgetItem('Н/Д'))  # # Авария - предупреждение сопр. шлейфа
					self.tblitems_1.item(k, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
					self.tblitems_1.item(k, i).setBackground(QtGui.QColor(208, 210, 177))  # серый
					self.tblitems_1.item(k, i, ).setForeground(QtGui.QColor(0, 0, 0))
		if block_start1 == 1:
			for k in [13, 14, 15, 16, 17, 18, 19, 21, 22, 23, 24, 25, 26]:
				for i in range(10):
					self.tblitems_1.setItem(k, i, QTableWidgetItem('Н/Д'))  # # Авария - предупреждение сопр. шлейфа
					self.tblitems_1.item(k, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
					self.tblitems_1.item(k, i).setBackground(QtGui.QColor(208, 210, 177))  # серый
					self.tblitems_1.item(k, i, ).setForeground(QtGui.QColor(0, 0, 0))
			for k in [1, 2, 3]:
				for i in range(10):
					self.tblitems_d.setItem(k, i, QTableWidgetItem('Н/Д'))  # блокировка  значения по RS плата 1
					self.tblitems_d.item(k, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
					self.tblitems_d.item(k, i).setBackground(QtGui.QColor(208, 210, 177))  # серый
					self.tblitems_d.item(k, i, ).setForeground(QtGui.QColor(0, 0, 0))
		blok_RS = int(dataP4[4][0])
		if blok_RS == 1:
			for k in [1, 3, 4, 5, 6, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 21, 22, 23, 24, 25, 26]:
				for i in range(10):
					self.tblitems_1.setItem(k, i, QTableWidgetItem('Н/Д'))  # блокировка  значения по RS плата 1
					self.tblitems_1.item(k, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
					self.tblitems_1.item(k, i).setBackground(QtGui.QColor(208, 210, 177))  # серый
					self.tblitems_1.item(k, i, ).setForeground(QtGui.QColor(0, 0, 0))
			for k in range(6):
				for i in range(1):
					self.tableWidget_PMK.setItem(k, i, QTableWidgetItem('Н/Д'))  # блокировка  значения по RS устр - во
					self.tableWidget_PMK.item(k, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
					self.tableWidget_PMK.item(k, i).setBackground(QtGui.QColor(208, 210, 177))  # серый
					self.tableWidget_PMK.item(k, i, ).setForeground(QtGui.QColor(0, 0, 0))
			for k in [1, 2, 3, 5, 6, 7]:
				for i in range(10):
					self.tblitems_d.setItem(k, i, QTableWidgetItem('Н/Д'))  # блокировка  значения по RS плата 1
					self.tblitems_d.item(k, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
					self.tblitems_d.item(k, i).setBackground(QtGui.QColor(208, 210, 177))  # серый
					self.tblitems_d.item(k, i, ).setForeground(QtGui.QColor(0, 0, 0))
		blok_ID1 = int(dataP4[5][0])
		if blok_ID1 == 1:
			for k in [1, 3, 4, 5, 6, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 21, 22, 23, 24, 25, 26]:
				for i in range(10):
					self.tblitems_1.setItem(k, i, QTableWidgetItem('Н/Д'))  # блокировка  значения по RS плата 1
					self.tblitems_1.item(k, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
					self.tblitems_1.item(k, i).setBackground(QtGui.QColor(208, 210, 177))  # серый
					self.tblitems_1.item(k, i, ).setForeground(QtGui.QColor(0, 0, 0))
			for k in [1, 2, 3]:
				for i in range(10):
					self.tblitems_d.setItem(k, i, QTableWidgetItem('Н/Д'))  # блокировка  значения по RS плата 1
					self.tblitems_d.item(k, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
					self.tblitems_d.item(k, i).setBackground(QtGui.QColor(208, 210, 177))  # серый
					self.tblitems_d.item(k, i, ).setForeground(QtGui.QColor(0, 0, 0))
		"""
		Блокировка отображения 2
		"""
		for i in range(10):
			modeCh2 = int(dataP2[0][i])
			if modeCh2 == 9:
				for k in [13, 14, 15, 16, 17, 18, 19, 21, 22, 23, 24, 25, 26]:
					self.tblitems_2.setItem(k, i, QTableWidgetItem('Н/Д'))
					self.tblitems_2.item(k, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
					self.tblitems_2.item(k, i).setBackground(QtGui.QColor(208, 210, 177))  # серый
					self.tblitems_2.item(k, i, ).setForeground(QtGui.QColor(0, 0, 0))
		if block_start2 == 1:
			for k in [13, 14, 15, 16, 17, 18, 19, 21, 22, 23, 24, 25, 26]:
				for i in range(10):
					self.tblitems_2.setItem(k, i, QTableWidgetItem('Н/Д'))  # # Авария - предупреждение сопр. шлейфа
					self.tblitems_2.item(k, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
					self.tblitems_2.item(k, i).setBackground(QtGui.QColor(208, 210, 177))  # серый
					self.tblitems_2.item(k, i, ).setForeground(QtGui.QColor(0, 0, 0))
			for k in [5, 6, 7]:
				for i in range(10):
					self.tblitems_d.setItem(k, i, QTableWidgetItem('Н/Д'))  # блокировка  значения по RS плата 1
					self.tblitems_d.item(k, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
					self.tblitems_d.item(k, i).setBackground(QtGui.QColor(208, 210, 177))  # серый
					self.tblitems_d.item(k, i, ).setForeground(QtGui.QColor(0, 0, 0))
		blok_RS = dataP4[4][1]
		if blok_RS == 1:
			for k in [1, 3, 4, 5, 6, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 21, 22, 23, 24, 25, 26]:
				for i in range(10):
					self.tblitems_2.setItem(k, i, QTableWidgetItem('Н/Д'))  # блокировка  значения по RS плата 1
					self.tblitems_2.item(k, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
					self.tblitems_2.item(k, i).setBackground(QtGui.QColor(208, 210, 177))  # серый
					self.tblitems_2.item(k, i, ).setForeground(QtGui.QColor(0, 0, 0))
			for k in range(6):
				for i in range(1):
					self.tableWidget_PMK.setItem(k, i, QTableWidgetItem('Н/Д'))  # блокировка  значения по RS устр - во
					self.tableWidget_PMK.item(k, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
					self.tableWidget_PMK.item(k, i).setBackground(QtGui.QColor(208, 210, 177))  # серый
					self.tableWidget_PMK.item(k, i, ).setForeground(QtGui.QColor(0, 0, 0))
			for k in [1, 2, 3]:
				for i in range(10):
					self.tblitems_d.setItem(k, i, QTableWidgetItem('Н/Д'))  # блокировка  значения по RS плата 1
					self.tblitems_d.item(k, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
					self.tblitems_d.item(k, i).setBackground(QtGui.QColor(208, 210, 177))  # серый
					self.tblitems_d.item(k, i, ).setForeground(QtGui.QColor(0, 0, 0))
		blok_ID2 = int(dataP4[5][1])
		if blok_ID2 == 1:
			for k in [1, 3, 4, 5, 6, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 21, 22, 23, 24, 25, 26]:
				for i in range(10):
					self.tblitems_2.setItem(k, i, QTableWidgetItem('Н/Д'))  # блокировка  значения по RS плата 1
					self.tblitems_2.item(k, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
					self.tblitems_2.item(k, i).setBackground(QtGui.QColor(208, 210, 177))  # серый
					self.tblitems_2.item(k, i, ).setForeground(QtGui.QColor(0, 0, 0))
			for k in [5, 6, 7]:
				for i in range(10):
					self.tblitems_d.setItem(k, i, QTableWidgetItem('Н/Д'))  # блокировка  значения по RS плата 1
					self.tblitems_d.item(k, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
					self.tblitems_d.item(k, i).setBackground(QtGui.QColor(208, 210, 177))  # серый
					self.tblitems_d.item(k, i, ).setForeground(QtGui.QColor(0, 0, 0))
		"""
		Блокировка отображения 1-2
		"""
		if ((blok_ID1 == 1) & (blok_ID2 == 1)) == 1:
			for k in range(6):
				for i in range(1):
					self.tableWidget_PMK.setItem(k, i, QTableWidgetItem('Н/Д'))  # блокировка  значения по RS устр - во
					self.tableWidget_PMK.item(k, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
					self.tableWidget_PMK.item(k, i).setBackground(QtGui.QColor(208, 210, 177))  # серый
					self.tableWidget_PMK.item(k, i, ).setForeground(QtGui.QColor(0, 0, 0))

	# self.tableWidget.setItem (1, 1, QTableWidgetItem ("УКККФ"))		#(dataP4[0][0]))

	# self.table.close()
	# self.table.show()
	# self.endResetModel()
	# self.tableView.setModel(PandasModel)
	# time.sleep(5)

	def defAddMb(self):
		# self.lineEdit_1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)

		tCombo1 = int(self.comboBox_1.currentText(), 16)
		tCombo2 = int(self.comboBox_2.currentText(), 16)
		intCombo = tCombo1 * 16 + tCombo2
		# dat.set_id_serial (intCombo)

		print('ВВеден номер = ', intCombo)
		dataP4[0][0] = intCombo


# self.tblitems_2.setItem (1, 1, QTableWidgetItem ("Ура!!!!!", ))


# endregion
data = np.array([[1, 9, 2], [1, 0, -1], [3, 5, 2], [3, 3, 2], [5, 8, 9], ])


def mDB(array):

	try:
		# Подключение к существующей базе данных
		connection = psycopg2.connect(user = "postgres", # пароль, который указали при установке PostgreSQL
			password = "123", host = "127.0.0.1", port = "5432")
		connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
		# Курсор для выполнения операций с базой данных
		cursor = connection.cursor()
		sql_create_database = 'create database pmk20_db'
		cursor.execute(sql_create_database)
	except (Exception, Error) as error:
		print("Ошибка при работе с PostgreSQL", error)
	finally:
		if connection:
			cursor.close()
			connection.close()
			print("Соединение с PostgreSQL закрыто")
	time.sleep(2)
	try:
		# Подключиться к существующей базе данных
		connection = psycopg2.connect(user = "postgres", # пароль, который указали при установке PostgreSQL
			password = "123", host = "127.0.0.1", port = "5432", database = "pmk20_db")

		# Создайте курсор для выполнения операций с базой данных
		cursor = connection.cursor()
		# SQL-запрос для создания новой таблицы
		create_table_query = '''CREATE TABLE pmk
	                          ( 
	                            c_id SERIAL PRIMARY KEY,
	                            TIME            TIMESTAMPTZ,
	                            IDPMK           TEXT,
	                            NumPlat         INT,
	                            NumCh           INT,
	                            Uinput1         FLOAT,
	                            Uinput2         FLOAT,
	                            RZ1             FLOAT,
	                            RZ2             FLOAT,
	                            RLOOP           FLOAT,
	                            Uvol            FLOAT
	                            ); '''
		# Выполнение команды: это создает новую таблицу
		cursor.execute(create_table_query)
		connection.commit()
		print("Таблица успешно создана в PostgreSQL")

	except (Exception, Error) as error:
		print("Ошибка при работе с PostgreSQL", error)
	finally:
		if connection:
			cursor.close()
			connection.close()
			print("Соединение с PostgreSQL закрыто")

	dataAll = frombuffer(array, dtype = double, count = len(array))
	dataAll.fill(1.0)
	# reshape array into preferred shape
	dataAll = dataAll.reshape((26, 40))
	dataSumm = np.hsplit(dataAll, 4)
	dataP1 = dataSumm[0]
	dataP2 = dataSumm[1]
	dataP3 = dataSumm[2]
	dataP4 = dataSumm[3]
	setMode0 = 0
	setMode1 = 0
	startLoad = 0
	while (1):
		modePMK1 = int (dataP4[1][1])
		modePMK2 = int (dataP4[10][1])
		modePMK = 0
		ErrorCon1 = int (dataP4[5][0])
		ErrorCon2 = int (dataP4[5][1])
		_idPMK1 = dataP4[1][3]
		_idPMK2 = dataP4[10][3]
		_idPMK = 0
		start1 = int(dataP4[3][0])
		start2 = int(dataP4[13][0])
		# modeSh2 = dataP2[0]
		# modeSh1 = dataP1[0]

		# numPat  = int (dataP4[18][0])

		if ErrorCon1 == 0:
			if modePMK1 == 1:
				setMode0 = 1
				# startLoad = 0
			elif ((modePMK1 == 10) & (setMode0 == 1)) == 1:
				startLoad = 1
				setMode0 = 0
			_idPMK = int(_idPMK1)

		elif ErrorCon2 == 0:
			if modePMK2 == 1:
				setMode0 = 1
				# startLoad = 0
			elif(modePMK2 == 10) & (setMode0 == 1) == 1:
				startLoad = 1
				setMode0 = 0
			_idPMK = int(_idPMK2)
		else:
			startLoad = 0

		# print('START LOAD = ', startLoad)
		# startLoad =1

		if startLoad == 1:
			print("СТАРТ ЗАПИСИ SQL !!!")

			if ((start1 == 1) & (ErrorCon1 == 0)) ==1:
				print("СТАРТ ЗАПИСИ TABLE 1")
			# startLoad = 0
				idPMK = int(_idPMK1)
				idPMK = str(hex(idPMK))

				NumPlat = 1
				for i in range (10):
					if ((dataP1[0][i] != 0)&
						(dataP1[0][i] != 1)&
						(dataP1[0][i] != 3)&
						(dataP1[0][i] != 4)&
						(dataP1[0][i] != 5)&
						(dataP1[0][i] != 9)):
						NumCh = i+1
						Uinput1 = (dataP1[12][i]/10)
						Uinput2 = (dataP1[13][i]/10)
						RZ1 = dataP1[9][i]
						RZ2 = dataP1[10][i]
						Rloop = dataP1[11][i]
						Uvol = round (dataP1[14][i],2)

						try:
							# t = str(time.time())
							# # print(t)
							# t = '2014-04-04 20:00:00'
							# Подключиться к существующей базе данных
							connection = psycopg2.connect(user = "postgres", # пароль, который указали при установке PostgreSQL
								password = "123", host = "127.0.0.1", port = "5432", database = "pmk20_db")
							cursor = connection.cursor()

							# Выполнение SQL-запроса для вставки данных в таблицу
							insert_query_db = """ INSERT INTO pmk (                           
													TIME            ,
													IDPMK           ,                                  
													NumPlat         ,
													NumCh           ,
													Uinput1         ,
													Uinput2         ,
													Rz1             ,
													Rz2             ,
													Rloop           ,
													Uvol                      
														)  
													VALUES (CURRENT_TIMESTAMP, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
							cursor.execute(insert_query_db, (idPMK , NumPlat, NumCh, Uinput1, Uinput2, RZ1, RZ2, Rloop, Uvol ))
							connection.commit()
							print("1 запись успешно вставлена")
							# Получить результат
							cursor.execute("SELECT * from pmk")
							record = cursor.fetchall()
							print("Результат", record)

						# # Выполнение SQL-запроса для обновления таблицы  # update_query = """Update pmk set price = 1500 where id = 1"""  # cursor.execute(update_query)  # connection.commit()  # count = cursor.rowcount  # print(count, "Запись успешно удалена")  # # Получить результат  # cursor.execute("SELECT * from mobile")  # print("Результат", cursor.fetchall())  #  # # Выполнение SQL-запроса для удаления таблицы  # delete_query = """Delete from mobile where id = 1"""  # cursor.execute(delete_query)  # connection.commit()  # count = cursor.rowcount  # print(count, "Запись успешно удалена")  # # Получить результат  # cursor.execute("SELECT * from mobile")  # print("Результат", cursor.fetchall())

						except (Exception, Error) as error:
							print("Ошибка при работе с PostgreSQL", error)
						finally:
							if connection:
								cursor.close()
								connection.close()
								print("Соединение с PostgreSQL закрыто")

			if ((start2 == 1) & (ErrorCon2 == 0)) ==1:
				idPMK = int(_idPMK2)
				idPMK = str(hex(idPMK))
				print("СТАРТ ЗАПИСИ TABLE 2")
				NumPlat = 2
				for i in range(10):
					if ((dataP2[0][i] != 0)&
						(dataP2[0][i] != 1)&
						(dataP2[0][i] != 3)&
						(dataP2[0][i] != 4)&
						(dataP2[0][i] != 5)&
						(dataP2[0][i] != 9)):
						NumCh = i+1
						Uinput1 = (dataP2[12][i]/10)
						Uinput2 = (dataP2[13][i]/10)
						RZ1 = dataP2[9][i]
						RZ2 = dataP2[10][i]
						Rloop = dataP2[11][i]
						Uvol = round(dataP2[14][i], 2)
						try:
							t = str(time.time())
							print(t)
							t = '2014-04-04 20:00:00'
							# Подключиться к существующей базе данных
							connection = psycopg2.connect(user = "postgres",  # пароль, который указали при установке PostgreSQL
								password = "123", host = "127.0.0.1", port = "5432", database = "pmk20_db")
							cursor = connection.cursor()

							# Выполнение SQL-запроса для вставки данных в таблицу
							insert_query_db = """ INSERT INTO pmk (                           
																TIME            ,
																IDPMK           ,                                  
																NumPlat         ,
																NumCh           ,
																Uinput1         ,
																Uinput2         ,
																Rz1             ,
																Rz2             ,
																Rloop           ,
																Uvol                      
																	)  
																VALUES (CURRENT_TIMESTAMP, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
							cursor.execute(insert_query_db, (idPMK, NumPlat, NumCh, Uinput1, Uinput2, RZ1, RZ2, Rloop, Uvol))
							connection.commit()
							print("1 запись успешно вставлена")
							# Получить результат
							cursor.execute("SELECT * from pmk")
							record = cursor.fetchall()
							print("Результат", record)

						# # Выполнение SQL-запроса для обновления таблицы  # update_query = """Update pmk set price = 1500 where id = 1"""  # cursor.execute(update_query)  # connection.commit()  # count = cursor.rowcount  # print(count, "Запись успешно удалена")  # # Получить результат  # cursor.execute("SELECT * from mobile")  # print("Результат", cursor.fetchall())  #  # # Выполнение SQL-запроса для удаления таблицы  # delete_query = """Delete from mobile where id = 1"""  # cursor.execute(delete_query)  # connection.commit()  # count = cursor.rowcount  # print(count, "Запись успешно удалена")  # # Получить результат  # cursor.execute("SELECT * from mobile")  # print("Результат", cursor.fetchall())

						except (Exception, Error) as error:
							print("Ошибка при работе с PostgreSQL", error)
						finally:
							if connection:
								cursor.close()
								connection.close()
								print("Соединение с PostgreSQL закрыто")

			startLoad = 0
		# time.sleep(1)


# region Task(array)
# task executed in a child process
def task(array):
	# create a new numpy array backed by the raw array
	dataAll = frombuffer(array, dtype = double, count = len(array))
	# reshape array into preferred shape
	dataAll = dataAll.reshape((26, 40))
	dataSumm = np.hsplit(dataAll, 4)
	dataP1 = dataSumm[0]
	dataP2 = dataSumm[1]
	dataP3 = dataSumm[2]
	dataP4 = dataSumm[3]

	# check the contents
	# print(f'Child\n{dataP2}')

	mB = myModbus()
	# increment the data
	while (True):
		# dataP1[:] += 1
		# dataP1[1][1] = str ( 300 )
		# dataP2[:] += 20
		# confirm change
		# print (f'Child\n{dataP4}')
		time.sleep(1)
		# print ('P4 00 = ', dataP4[0][0])
		mB.setDataP1(dataP1)
		mB.setDataP2(dataP2)
		mB.setDataP3(dataP3)
		mB.setDataP4(dataP4)
		mB.con_1()
		mB.con_2()
		mB.getDataP1()
		mB.getDataP2()
		mB.getDataP3()
		mB.getDataP4()


# endregion

# region Visu(array)
def visu(array):
	dataAll = frombuffer(array, dtype = double, count = len(array))
	# reshape array into preferred shape
	dataAll = dataAll.reshape((26, 40))
	dataSumm = np.hsplit(dataAll, 4)
	# while(True):
	dataP1 = dataSumm[0]
	dataP2 = dataSumm[1]
	dataP3 = dataSumm[2]

	dataP4 = dataSumm[3]

	# dataP1[1][2] = 25
	# dataP2[1][2] = 500 + 1
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	window.update_table()
	# time.sleep(1)
	app.exec()


# endregion
# protect the entry point
if __name__ == "__main__":
	# define the size of the numpy array
	n = 26 * 40
	# create the shared array
	array = RawArray('d', n)
	# create a new numpy array backed by the raw array

	dataAll = frombuffer(array, dtype = double, count = len(array))

	# reshape array into preferred shape
	dataAll = dataAll.reshape(26, 40)
	# populate the array
	dataAll.fill(1.0)
	dataSumm = np.hsplit(dataAll, 4)
	dataP1 = dataSumm[0]
	dataP2 = dataSumm[1]
	dataP3 = dataSumm[2]
	dataP4 = dataSumm[3]

	# dataP1 = pd.DataFrame (dataP1,
	# 	columns = ['Калал 1', 'Калал 2', 'Калал 3', 'Калал 4', 'Калал 5',
	# 			   'Калал 6', 'Калал 7', 'Калал 8', 'Калал 9', 'Калал 10'],
	# 	index = ['Режим работы:', 'Режим работы канала', 'Допустимые диапазоны:',
	# 			 'Диапазон сопр. изоляции авар.',
	# 			 'Диапазон сопр. шлейфа авар.', 'Диапазон сопр. изоляции предупр.',
	# 			 'Диапазон сопр. шлейфа предупр.',
	# 			 'Уставки:', 'Уставка напряжения на входе', 'Уставка сопр. изоляции 1',
	# 			 'Уставка сопр. изоляции 2',
	# 			 'Уставка сопр. шлейфа', 'Текущие значения:', 'Сопр. изоляции 1', 'Сопр. изоляции 1',
	# 			 'Сопр. шлейфа', 'Напряжение на входе 1', 'Напряжение на входе 2',
	# 			 'Расчетное знач. объем. наряжение', 'Авария - "А", предупрежд. - "П"',
	# 			 'Сопр. изоляции 1 ниже доп.',
	# 			 'Сопр. изоляции 2 ниже доп.', 'Сопр. шлейфа ниже доп.', 'Сопр. шлейфа выше доп.',
	# 			 'Напряжение на входе 1 выше доп.', 'Напряжение на входе 2 выше доп.'])

	dataP3 = pd.DataFrame(dataP3,
		columns = ['Дата/время', 'Калал 2', 'Калал 3', 'Калал 4', 'Калал 5', 'Калал 6', 'Калал 7', 'Калал 8', 'Калал 9',
			'Калал 10'],
		index = ['Режим работы:', 'Режим работы канала', 'Допустимые диапазоны:', 'Диапазон сопр. изоляции авар.',
			'Диапазон сопр. шлейфа авар.', 'Диапазон сопр. изоляции предупр.', 'Диапазон сопр. шлейфа предупр.',
			'Уставки:', 'Уставка напряжения на входе', 'Уставка сопр. изоляции 1', 'Уставка сопр. изоляции 2',
			'Уставка сопр. шлейфа', 'Текущие значения:', 'Сопр. изоляции 1', 'Сопр. изоляции 1', 'Сопр. шлейфа',
			'Напряжение на входе 1', 'Напряжение на входе 2', 'Расчетное знач. объем. наряжение',
			'Авария - "А", предупрежд. - "П"', 'Сопр. изоляции 1 ниже доп.', 'Сопр. изоляции 2 ниже доп.',
			'Сопр. шлейфа ниже доп.', 'Сопр. шлейфа выше доп.', 'Напряжение на входе 1 выше доп.',
			'Напряжение на входе 2 выше доп.'])

	# confirm contents of the new array
	# print(f'Parent\n{data}')
	# create a child process
	child1 = Process(target = task, args = (array,), daemon = True)
	child2 = Process(target = visu, args = (array,), daemon = True)
	child3 = Process(target = mDB, args = (array,), daemon = True)
	# start the child process
	child3.start()
	child2.start()
	child1.start()
	# wait for the child process to complete

	child2.join()
	# check some data in the shared array

	# print(f'Parent\n{data}')
