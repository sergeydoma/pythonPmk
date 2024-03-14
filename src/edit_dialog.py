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
        MainWindow.setStyleSheet(u"background-color: rgb(213, 213, 159);")
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
        self.tableWidget = QTableWidget(self.tab_1)
        if (self.tableWidget.columnCount() < 1):
            self.tableWidget.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        if (self.tableWidget.rowCount() < 7):
            self.tableWidget.setRowCount(7)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignJustify|Qt.AlignVCenter);
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setItem(1, 0, __qtablewidgetitem9)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(680, 50, 711, 241))
        font1 = QFont()
        font1.setFamilies([u"Sans Serif"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setKerning(True)
        font1.setHintingPreference(QFont.PreferFullHinting)
        self.tableWidget.setFont(font1)
        self.tableWidget.setStyleSheet(u"border-color: rgb(0, 85, 0);")
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(470)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setStretchLastSection(True)
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
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tblitems_d.setHorizontalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tblitems_d.setHorizontalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tblitems_d.setHorizontalHeaderItem(2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tblitems_d.setHorizontalHeaderItem(3, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tblitems_d.setHorizontalHeaderItem(4, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tblitems_d.setHorizontalHeaderItem(5, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tblitems_d.setHorizontalHeaderItem(6, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tblitems_d.setHorizontalHeaderItem(7, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tblitems_d.setHorizontalHeaderItem(8, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tblitems_d.setHorizontalHeaderItem(9, __qtablewidgetitem19)
        if (self.tblitems_d.rowCount() < 8):
            self.tblitems_d.setRowCount(8)
        font2 = QFont()
        font2.setBold(True)
        font2.setItalic(True)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setFont(font2);
        self.tblitems_d.setVerticalHeaderItem(0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tblitems_d.setVerticalHeaderItem(1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tblitems_d.setVerticalHeaderItem(2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tblitems_d.setVerticalHeaderItem(3, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setFont(font2);
        self.tblitems_d.setVerticalHeaderItem(4, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tblitems_d.setVerticalHeaderItem(5, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tblitems_d.setVerticalHeaderItem(6, __qtablewidgetitem26)
        icon = QIcon(QIcon.fromTheme(u"accessories-calculator"))
        __qtablewidgetitem27 = QTableWidgetItem()
        __qtablewidgetitem27.setText(u"\u041d\u0435\u0438\u0441\u043f\u0440\u0430\u0432\u043d\u043e\u0441\u0442\u044c \u0441\u043c\u0435\u0449\u0435\u043d\u0438\u044f -100 \u0412");
        __qtablewidgetitem27.setIcon(icon);
        self.tblitems_d.setVerticalHeaderItem(7, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        __qtablewidgetitem28.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled|Qt.ItemIsAutoTristate);
        self.tblitems_d.setItem(6, 0, __qtablewidgetitem28)
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
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tblitems_1.setHorizontalHeaderItem(0, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tblitems_1.setHorizontalHeaderItem(1, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tblitems_1.setHorizontalHeaderItem(2, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tblitems_1.setHorizontalHeaderItem(3, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tblitems_1.setHorizontalHeaderItem(4, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tblitems_1.setHorizontalHeaderItem(5, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tblitems_1.setHorizontalHeaderItem(6, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tblitems_1.setHorizontalHeaderItem(7, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tblitems_1.setHorizontalHeaderItem(8, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tblitems_1.setHorizontalHeaderItem(9, __qtablewidgetitem38)
        if (self.tblitems_1.rowCount() < 27):
            self.tblitems_1.setRowCount(27)
        __qtablewidgetitem39 = QTableWidgetItem()
        __qtablewidgetitem39.setFont(font2);
        self.tblitems_1.setVerticalHeaderItem(0, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tblitems_1.setVerticalHeaderItem(1, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        __qtablewidgetitem41.setFont(font2);
        self.tblitems_1.setVerticalHeaderItem(2, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.tblitems_1.setVerticalHeaderItem(3, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.tblitems_1.setVerticalHeaderItem(4, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.tblitems_1.setVerticalHeaderItem(5, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.tblitems_1.setVerticalHeaderItem(6, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        __qtablewidgetitem46.setFont(font2);
        self.tblitems_1.setVerticalHeaderItem(7, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.tblitems_1.setVerticalHeaderItem(8, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.tblitems_1.setVerticalHeaderItem(9, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        __qtablewidgetitem49.setText(u"\u0423\u0441\u0442\u0430\u0432\u043a\u0430 \u0441\u043e\u043f\u0440. \u0438\u0437\u043e\u043b\u044f\u0446\u0438\u0438 2 (\u041c\u041e\u043c)");
        __qtablewidgetitem49.setIcon(icon);
        self.tblitems_1.setVerticalHeaderItem(10, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.tblitems_1.setVerticalHeaderItem(11, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        __qtablewidgetitem51.setFont(font2);
        self.tblitems_1.setVerticalHeaderItem(12, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.tblitems_1.setVerticalHeaderItem(13, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.tblitems_1.setVerticalHeaderItem(14, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.tblitems_1.setVerticalHeaderItem(15, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        self.tblitems_1.setVerticalHeaderItem(16, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        self.tblitems_1.setVerticalHeaderItem(17, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        self.tblitems_1.setVerticalHeaderItem(18, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        self.tblitems_1.setVerticalHeaderItem(19, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        __qtablewidgetitem59.setFont(font2);
        self.tblitems_1.setVerticalHeaderItem(20, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        self.tblitems_1.setVerticalHeaderItem(21, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        self.tblitems_1.setVerticalHeaderItem(22, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        self.tblitems_1.setVerticalHeaderItem(23, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        self.tblitems_1.setVerticalHeaderItem(24, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        self.tblitems_1.setVerticalHeaderItem(25, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        self.tblitems_1.setVerticalHeaderItem(26, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        __qtablewidgetitem66.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled|Qt.ItemIsAutoTristate);
        self.tblitems_1.setItem(9, 0, __qtablewidgetitem66)
        __qtablewidgetitem67 = QTableWidgetItem()
        __qtablewidgetitem67.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(21, 0, __qtablewidgetitem67)
        __qtablewidgetitem68 = QTableWidgetItem()
        __qtablewidgetitem68.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(21, 1, __qtablewidgetitem68)
        __qtablewidgetitem69 = QTableWidgetItem()
        __qtablewidgetitem69.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(21, 2, __qtablewidgetitem69)
        __qtablewidgetitem70 = QTableWidgetItem()
        __qtablewidgetitem70.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(21, 3, __qtablewidgetitem70)
        __qtablewidgetitem71 = QTableWidgetItem()
        __qtablewidgetitem71.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(21, 4, __qtablewidgetitem71)
        __qtablewidgetitem72 = QTableWidgetItem()
        __qtablewidgetitem72.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(21, 5, __qtablewidgetitem72)
        __qtablewidgetitem73 = QTableWidgetItem()
        __qtablewidgetitem73.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(21, 6, __qtablewidgetitem73)
        __qtablewidgetitem74 = QTableWidgetItem()
        __qtablewidgetitem74.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(21, 7, __qtablewidgetitem74)
        __qtablewidgetitem75 = QTableWidgetItem()
        __qtablewidgetitem75.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(21, 8, __qtablewidgetitem75)
        __qtablewidgetitem76 = QTableWidgetItem()
        __qtablewidgetitem76.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(21, 9, __qtablewidgetitem76)
        __qtablewidgetitem77 = QTableWidgetItem()
        __qtablewidgetitem77.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(22, 0, __qtablewidgetitem77)
        __qtablewidgetitem78 = QTableWidgetItem()
        __qtablewidgetitem78.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(22, 1, __qtablewidgetitem78)
        __qtablewidgetitem79 = QTableWidgetItem()
        __qtablewidgetitem79.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(22, 2, __qtablewidgetitem79)
        __qtablewidgetitem80 = QTableWidgetItem()
        __qtablewidgetitem80.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(22, 3, __qtablewidgetitem80)
        __qtablewidgetitem81 = QTableWidgetItem()
        __qtablewidgetitem81.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(22, 4, __qtablewidgetitem81)
        __qtablewidgetitem82 = QTableWidgetItem()
        __qtablewidgetitem82.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(22, 5, __qtablewidgetitem82)
        __qtablewidgetitem83 = QTableWidgetItem()
        __qtablewidgetitem83.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(22, 6, __qtablewidgetitem83)
        __qtablewidgetitem84 = QTableWidgetItem()
        __qtablewidgetitem84.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(22, 7, __qtablewidgetitem84)
        __qtablewidgetitem85 = QTableWidgetItem()
        __qtablewidgetitem85.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(22, 8, __qtablewidgetitem85)
        __qtablewidgetitem86 = QTableWidgetItem()
        __qtablewidgetitem86.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(22, 9, __qtablewidgetitem86)
        __qtablewidgetitem87 = QTableWidgetItem()
        __qtablewidgetitem87.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(23, 0, __qtablewidgetitem87)
        __qtablewidgetitem88 = QTableWidgetItem()
        __qtablewidgetitem88.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(23, 1, __qtablewidgetitem88)
        __qtablewidgetitem89 = QTableWidgetItem()
        __qtablewidgetitem89.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(23, 2, __qtablewidgetitem89)
        __qtablewidgetitem90 = QTableWidgetItem()
        __qtablewidgetitem90.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(23, 3, __qtablewidgetitem90)
        __qtablewidgetitem91 = QTableWidgetItem()
        __qtablewidgetitem91.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(23, 4, __qtablewidgetitem91)
        __qtablewidgetitem92 = QTableWidgetItem()
        __qtablewidgetitem92.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(23, 5, __qtablewidgetitem92)
        __qtablewidgetitem93 = QTableWidgetItem()
        __qtablewidgetitem93.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(23, 6, __qtablewidgetitem93)
        __qtablewidgetitem94 = QTableWidgetItem()
        __qtablewidgetitem94.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(23, 7, __qtablewidgetitem94)
        __qtablewidgetitem95 = QTableWidgetItem()
        __qtablewidgetitem95.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(23, 8, __qtablewidgetitem95)
        __qtablewidgetitem96 = QTableWidgetItem()
        __qtablewidgetitem96.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(23, 9, __qtablewidgetitem96)
        __qtablewidgetitem97 = QTableWidgetItem()
        __qtablewidgetitem97.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(24, 0, __qtablewidgetitem97)
        __qtablewidgetitem98 = QTableWidgetItem()
        __qtablewidgetitem98.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(24, 1, __qtablewidgetitem98)
        __qtablewidgetitem99 = QTableWidgetItem()
        __qtablewidgetitem99.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(24, 2, __qtablewidgetitem99)
        __qtablewidgetitem100 = QTableWidgetItem()
        __qtablewidgetitem100.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(24, 3, __qtablewidgetitem100)
        __qtablewidgetitem101 = QTableWidgetItem()
        __qtablewidgetitem101.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(24, 4, __qtablewidgetitem101)
        __qtablewidgetitem102 = QTableWidgetItem()
        __qtablewidgetitem102.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(24, 5, __qtablewidgetitem102)
        __qtablewidgetitem103 = QTableWidgetItem()
        __qtablewidgetitem103.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(24, 6, __qtablewidgetitem103)
        __qtablewidgetitem104 = QTableWidgetItem()
        __qtablewidgetitem104.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(24, 7, __qtablewidgetitem104)
        __qtablewidgetitem105 = QTableWidgetItem()
        __qtablewidgetitem105.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(24, 8, __qtablewidgetitem105)
        __qtablewidgetitem106 = QTableWidgetItem()
        __qtablewidgetitem106.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(24, 9, __qtablewidgetitem106)
        __qtablewidgetitem107 = QTableWidgetItem()
        __qtablewidgetitem107.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(25, 0, __qtablewidgetitem107)
        __qtablewidgetitem108 = QTableWidgetItem()
        __qtablewidgetitem108.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(25, 1, __qtablewidgetitem108)
        __qtablewidgetitem109 = QTableWidgetItem()
        __qtablewidgetitem109.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(25, 2, __qtablewidgetitem109)
        __qtablewidgetitem110 = QTableWidgetItem()
        __qtablewidgetitem110.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(25, 3, __qtablewidgetitem110)
        __qtablewidgetitem111 = QTableWidgetItem()
        __qtablewidgetitem111.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(25, 4, __qtablewidgetitem111)
        __qtablewidgetitem112 = QTableWidgetItem()
        __qtablewidgetitem112.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(25, 5, __qtablewidgetitem112)
        __qtablewidgetitem113 = QTableWidgetItem()
        __qtablewidgetitem113.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(25, 6, __qtablewidgetitem113)
        __qtablewidgetitem114 = QTableWidgetItem()
        __qtablewidgetitem114.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(25, 7, __qtablewidgetitem114)
        __qtablewidgetitem115 = QTableWidgetItem()
        __qtablewidgetitem115.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(25, 8, __qtablewidgetitem115)
        __qtablewidgetitem116 = QTableWidgetItem()
        __qtablewidgetitem116.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(25, 9, __qtablewidgetitem116)
        __qtablewidgetitem117 = QTableWidgetItem()
        __qtablewidgetitem117.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(26, 0, __qtablewidgetitem117)
        __qtablewidgetitem118 = QTableWidgetItem()
        __qtablewidgetitem118.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(26, 1, __qtablewidgetitem118)
        __qtablewidgetitem119 = QTableWidgetItem()
        __qtablewidgetitem119.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(26, 2, __qtablewidgetitem119)
        __qtablewidgetitem120 = QTableWidgetItem()
        __qtablewidgetitem120.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(26, 3, __qtablewidgetitem120)
        __qtablewidgetitem121 = QTableWidgetItem()
        __qtablewidgetitem121.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(26, 4, __qtablewidgetitem121)
        __qtablewidgetitem122 = QTableWidgetItem()
        __qtablewidgetitem122.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(26, 5, __qtablewidgetitem122)
        __qtablewidgetitem123 = QTableWidgetItem()
        __qtablewidgetitem123.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(26, 6, __qtablewidgetitem123)
        __qtablewidgetitem124 = QTableWidgetItem()
        __qtablewidgetitem124.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(26, 7, __qtablewidgetitem124)
        __qtablewidgetitem125 = QTableWidgetItem()
        __qtablewidgetitem125.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(26, 8, __qtablewidgetitem125)
        __qtablewidgetitem126 = QTableWidgetItem()
        __qtablewidgetitem126.setTextAlignment(Qt.AlignCenter);
        self.tblitems_1.setItem(26, 9, __qtablewidgetitem126)
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
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tableView_Arhive = QTableView(self.tab_4)
        self.tableView_Arhive.setObjectName(u"tableView_Arhive")
        self.tableView_Arhive.setGeometry(QRect(10, 1, 1391, 841))
        self.tableView_Arhive.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(234, 232, 220);\n"
"")
        self.tableView_Arhive.setLineWidth(3)
        self.tableView_Arhive.setMidLineWidth(2)
        self.tableView_Arhive.setSortingEnabled(True)
        self.tabWidget.addTab(self.tab_4, "")

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
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435", None));
        ___qtablewidgetitem1 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0436\u0438\u043c \u0440\u0430\u0431\u043e\u0442\u044b \u043f\u0440\u0438\u0431\u043e\u0440\u0430", None));
        ___qtablewidgetitem2 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u043c\u0435\u0440 \u0432\u0435\u0440\u0441\u0438\u0438 \u041f\u041e", None));
        ___qtablewidgetitem3 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"ID \u0448\u0430\u0441\u0441\u0438", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"ID \u041f\u043b\u0430\u0442\u044b 1", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"ID \u041f\u043b\u0430\u0442\u044b 2", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043d\u0442\u0440\u043e\u043b\u044c\u043d\u0430\u044f \u0441\u0443\u043c\u043c\u0430 \u041f\u041e MD5", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u0435 \u043f\u0440\u0438\u0431\u043e\u0440\u0430", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem8 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"AA22", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

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

        ___qtablewidgetitem9 = self.tblitems_d.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043d\u0430\u043b 1", None));
        ___qtablewidgetitem10 = self.tblitems_d.horizontalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043d\u0430\u043b 2", None));
        ___qtablewidgetitem11 = self.tblitems_d.horizontalHeaderItem(2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043d\u0430\u043b 3", None));
        ___qtablewidgetitem12 = self.tblitems_d.horizontalHeaderItem(3)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043d\u0430\u043b 4", None));
        ___qtablewidgetitem13 = self.tblitems_d.horizontalHeaderItem(4)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043d\u0430\u043b 5", None));
        ___qtablewidgetitem14 = self.tblitems_d.horizontalHeaderItem(5)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043d\u0430\u043b 6", None));
        ___qtablewidgetitem15 = self.tblitems_d.horizontalHeaderItem(6)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043d\u0430\u043b 7", None));
        ___qtablewidgetitem16 = self.tblitems_d.horizontalHeaderItem(7)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043d\u0430\u043b 8", None));
        ___qtablewidgetitem17 = self.tblitems_d.horizontalHeaderItem(8)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043d\u0430\u043b 9", None));
        ___qtablewidgetitem18 = self.tblitems_d.horizontalHeaderItem(9)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043d\u0430\u043b 10", None));
        ___qtablewidgetitem19 = self.tblitems_d.verticalHeaderItem(0)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043b\u0430\u0442\u0430 1;", None));
        ___qtablewidgetitem20 = self.tblitems_d.verticalHeaderItem(1)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0438\u0441\u043f\u0440\u0430\u0432\u043d\u043e\u0432\u0442\u044c \u0410\u0426\u041f", None));
        ___qtablewidgetitem21 = self.tblitems_d.verticalHeaderItem(2)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0438\u0441\u043f\u0440\u0430\u0432\u043d\u043e\u0441\u0442\u044c \u0441\u043c\u0435\u0449\u0435\u043d\u0438\u044f +100 \u0412", None));
        ___qtablewidgetitem22 = self.tblitems_d.verticalHeaderItem(3)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0438\u0441\u043f\u0440\u0430\u0432\u043d\u043e\u0441\u0442\u044c \u0441\u043c\u0435\u0449\u0435\u043d\u0438\u044f -100 \u0412", None));
        ___qtablewidgetitem23 = self.tblitems_d.verticalHeaderItem(4)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043b\u0430\u0442\u0430 2:", None));
        ___qtablewidgetitem24 = self.tblitems_d.verticalHeaderItem(5)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0438\u0441\u043f\u0440\u0430\u0432\u043d\u043e\u0432\u0442\u044c \u0410\u0426\u041f", None));
        ___qtablewidgetitem25 = self.tblitems_d.verticalHeaderItem(6)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0438\u0441\u043f\u0440\u0430\u0432\u043d\u043e\u0441\u0442\u044c \u0441\u043c\u0435\u0449\u0435\u043d\u0438\u044f +100 \u0412", None));

        __sortingEnabled1 = self.tblitems_d.isSortingEnabled()
        self.tblitems_d.setSortingEnabled(False)
        self.tblitems_d.setSortingEnabled(__sortingEnabled1)

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0430\u0433\u043d\u043e\u0441\u0442\u0438\u043a\u0430 \u041f\u041c\u041a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QCoreApplication.translate("MainWindow", u"\u041f\u041c\u041a-20", None))
        ___qtablewidgetitem26 = self.tblitems_1.horizontalHeaderItem(0)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043d\u0430\u043b 1", None));
        ___qtablewidgetitem27 = self.tblitems_1.horizontalHeaderItem(1)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043d\u0430\u043b 2", None));
        ___qtablewidgetitem28 = self.tblitems_1.horizontalHeaderItem(2)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043d\u0430\u043b 3", None));
        ___qtablewidgetitem29 = self.tblitems_1.horizontalHeaderItem(3)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043d\u0430\u043b 4", None));
        ___qtablewidgetitem30 = self.tblitems_1.horizontalHeaderItem(4)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043d\u0430\u043b 5", None));
        ___qtablewidgetitem31 = self.tblitems_1.horizontalHeaderItem(5)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043d\u0430\u043b 6", None));
        ___qtablewidgetitem32 = self.tblitems_1.horizontalHeaderItem(6)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043d\u0430\u043b 7", None));
        ___qtablewidgetitem33 = self.tblitems_1.horizontalHeaderItem(7)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043d\u0430\u043b 8", None));
        ___qtablewidgetitem34 = self.tblitems_1.horizontalHeaderItem(8)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043d\u0430\u043b 9", None));
        ___qtablewidgetitem35 = self.tblitems_1.horizontalHeaderItem(9)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043d\u0430\u043b 10", None));
        ___qtablewidgetitem36 = self.tblitems_1.verticalHeaderItem(0)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0436\u0438\u043c\u044b \u0440\u0430\u0431\u043e\u0442\u044b:", None));
        ___qtablewidgetitem37 = self.tblitems_1.verticalHeaderItem(1)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0436\u0438\u043c \u0440\u0430\u0431\u043e\u0442\u044b \u043a\u0430\u043d\u0430\u043b\u0430", None));
        ___qtablewidgetitem38 = self.tblitems_1.verticalHeaderItem(2)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043f\u0443\u0441\u0442\u0438\u043c\u044b\u0435 \u0434\u0438\u0430\u043f\u0430\u0437\u043e\u043d\u044b:", None));
        ___qtablewidgetitem39 = self.tblitems_1.verticalHeaderItem(3)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0430\u043f\u0430\u0437\u043e\u043d \u0441\u043e\u043f\u0440. \u0438\u0437\u043e\u043b\u044f\u0446\u0438\u0438 \u0430\u0432\u0430\u0440. ", None));
        ___qtablewidgetitem40 = self.tblitems_1.verticalHeaderItem(4)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0430\u043f\u0430\u0437\u043e\u043d \u0441\u043e\u043f\u0440. \u0448\u043b\u0435\u0439\u0444\u0430 \u0430\u0432\u0430\u0440.", None));
        ___qtablewidgetitem41 = self.tblitems_1.verticalHeaderItem(5)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0430\u043f\u0430\u0437\u043e\u043d \u0441\u043e\u043f\u0440. \u0438\u0437\u043e\u043b\u044f\u0446\u0438\u0438 \u043f\u0440\u0435\u0434\u0443\u043f\u0440.", None));
        ___qtablewidgetitem42 = self.tblitems_1.verticalHeaderItem(6)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0430\u043f\u0430\u0437\u043e\u043d \u0441\u043e\u043f\u0440. \u0448\u043b\u0435\u0439\u0444\u0430 \u043f\u0440\u0435\u0434\u0443\u043f\u0440.", None));
        ___qtablewidgetitem43 = self.tblitems_1.verticalHeaderItem(7)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0441\u0442\u0430\u0432\u043a\u0438:", None));
        ___qtablewidgetitem44 = self.tblitems_1.verticalHeaderItem(8)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0441\u0442\u0430\u0432\u043a\u0430 \u043d\u0430\u043f\u0440\u044f\u0436\u0435\u043d\u0438\u044f \u043d\u0430 \u0432\u0445\u043e\u0434\u0435 (\u0412)", None));
        ___qtablewidgetitem45 = self.tblitems_1.verticalHeaderItem(9)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0441\u0442\u0430\u0432\u043a\u0430 \u0441\u043e\u043f\u0440. \u0438\u0437\u043e\u043b\u044f\u0446\u0438\u0438 1 (\u041c\u041e\u043c)", None));
        ___qtablewidgetitem46 = self.tblitems_1.verticalHeaderItem(11)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0441\u0442\u0430\u0432\u043a\u0430 \u0441\u043e\u043f\u0440. \u0448\u043b\u0435\u0439\u0444\u0430 (\u043a\u041e\u043c)", None));
        ___qtablewidgetitem47 = self.tblitems_1.verticalHeaderItem(12)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043a\u0443\u0449\u0438\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f:", None));
        ___qtablewidgetitem48 = self.tblitems_1.verticalHeaderItem(13)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u043f\u0440. \u0438\u0437\u043e\u043b\u044f\u0446\u0438\u0438 1 (\u041c\u041e\u043c)", None));
        ___qtablewidgetitem49 = self.tblitems_1.verticalHeaderItem(14)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u043f\u0440. \u0438\u0437\u043e\u043b\u044f\u0446\u0438\u0438 2 (\u041c\u041e\u043c)", None));
        ___qtablewidgetitem50 = self.tblitems_1.verticalHeaderItem(15)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u043f\u0440. \u0448\u043b\u0435\u0439\u0444\u0430 (\u043a\u041e\u043c)", None));
        ___qtablewidgetitem51 = self.tblitems_1.verticalHeaderItem(16)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u043f\u0440\u044f\u0436\u0435\u043d\u0438\u0435 \u043d\u0430 \u0432\u0445\u043e\u0434\u0435 1 (\u0412)", None));
        ___qtablewidgetitem52 = self.tblitems_1.verticalHeaderItem(17)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u043f\u0440\u044f\u0436\u0435\u043d\u0438\u0435 \u043d\u0430 \u0432\u0445\u043e\u0434\u0435 2 (\u0412)", None));
        ___qtablewidgetitem53 = self.tblitems_1.verticalHeaderItem(18)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0447\u0435\u0442\u043d\u043e\u0435 \u0437\u043d\u0430\u0447. \u043e\u0431\u044a\u0435\u043c. \u043d\u0430\u043f\u0440\u044f\u0436\u0435\u043d\u0438\u044f 1 (\u0412)", None));
        ___qtablewidgetitem54 = self.tblitems_1.verticalHeaderItem(19)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0447\u0435\u0442\u043d\u043e\u0435 \u0437\u043d\u0430\u0447. \u043e\u0431\u044a\u0435\u043c. \u043d\u0430\u043f\u0440\u044f\u0436\u0435\u043d\u0438\u044f 2 (\u0412)", None));
        ___qtablewidgetitem55 = self.tblitems_1.verticalHeaderItem(20)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0430\u0440\u0438\u0439\u043d\u044b\u0435 \u0441\u0438\u0433\u043d\u0430\u043b\u044b\":", None));
        ___qtablewidgetitem56 = self.tblitems_1.verticalHeaderItem(21)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u043f\u0440\u043e\u0442\u0438\u0432\u043b\u0435\u043d\u0438\u0435 \u0438\u0437\u043e\u043b\u044f\u0446\u0438\u0438 1 < \u0434\u043e\u043f.", None));
        ___qtablewidgetitem57 = self.tblitems_1.verticalHeaderItem(22)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u043f\u0440\u043e\u0442\u0438\u0432\u043b\u0435\u043d\u0438\u0435 \u0438\u0437\u043e\u043b\u044f\u0446\u0438\u0438 2 < \u0434\u043e\u043f.", None));
        ___qtablewidgetitem58 = self.tblitems_1.verticalHeaderItem(23)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u043f\u0440\u043e\u0442\u0438\u0432\u043b\u0435\u043d\u0438\u0435 \u0448\u043b\u0435\u0439\u0444\u0430 < \u0434\u043e\u043f.", None));
        ___qtablewidgetitem59 = self.tblitems_1.verticalHeaderItem(24)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u043f\u0440\u043e\u0442\u0438\u0432\u043b\u0435\u043d\u0438\u0435 \u0448\u043b\u0435\u0439\u0444\u0430 > \u0434\u043e\u043f.", None));
        ___qtablewidgetitem60 = self.tblitems_1.verticalHeaderItem(25)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u043f\u0440\u044f\u0436\u0435\u043d\u0438\u0435 1 \u0432\u044b\u0448\u0435 \u0434\u043e\u043f\u0443\u0441\u043a", None));
        ___qtablewidgetitem61 = self.tblitems_1.verticalHeaderItem(26)
        ___qtablewidgetitem61.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u043f\u0440\u044f\u0436\u0435\u043d\u0438\u0435 2 \u0432\u044b\u0448\u0435 \u0434\u043e\u043f\u0443\u0441\u043a", None));

        __sortingEnabled2 = self.tblitems_1.isSortingEnabled()
        self.tblitems_1.setSortingEnabled(False)
        self.tblitems_1.setSortingEnabled(__sortingEnabled2)

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u041f\u043b\u0430\u0442\u0430 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u041f\u043b\u0430\u0442\u0430 2", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"\u0410\u0440\u0445\u0438\u0432", None))
    # retranslateUi

