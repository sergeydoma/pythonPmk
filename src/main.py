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

from myModbus import myModbus
import time


import psycopg2
from psycopg2 import Error

# -*- coding: utf-8 -*-



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
from edit_dialog import Ui_MainWindow

#region Ui_MainWindow

#endregion






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
				self.label_info.setText("Нет связи с устройствами по адресу " + numID1 + ' и ' + numID2)
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
				self.label_info.setText("Нет связи с устройством по адресу " + numID1)
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
				self.label_info.setText("Нет связи с устройством по адресу " + numID2)
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
