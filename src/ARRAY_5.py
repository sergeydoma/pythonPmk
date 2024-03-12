# share 2d numpy array via a shared array
import ctypes
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
from myModbus import myModbus


# region Absract Model
class PandasModel (QAbstractTableModel):
	def __init__(self, data):
		super ().__init__ ()
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
		if index.isValid ():
			if role == Qt.DisplayRole or role == Qt.EditRole:
				value = self._data.iloc[index.row (), index.column ()]
				return str (value)
			if role == Qt.BackgroundRole and index.row () == 0:
				# See below for the data structure.
				return QtGui.QColor ('blue')
		if role == Qt.TextAlignmentRole:
			value = self._data.iloc[index.row ()][index.column ()]

			if isinstance (value, int) or isinstance (value, float) or isinstance (value, double):
				# Align right, vertical middle.
				return Qt.AlignVCenter + Qt.AlignRight

	def setData(self, index, value, role):
		if role == Qt.EditRole:
			try:
				value = int (value)
			except ValueError:
				return False
			self._data.iloc[index.row (), index.column ()] = value
			return True
		return False

	def flags(self, index):
		return Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable

	def headerData(self, section, orientation, role):
		# section is the index of the column/row.
		if role == Qt.DisplayRole:
			if orientation == Qt.Horizontal:
				return str (self._data.columns[section])

			if orientation == Qt.Vertical:
				return str (self._data.index[section])


# endregion
# region MainWindow
class MainWindow (QMainWindow, Ui_MainWindow):
	def __init__(self):
		super ().__init__ ()
		Ui_MainWindow.__init__ (self)
		self.setupUi (self)
		self.Button_con.clicked.connect (self.defAddMb)

		self.table = QTableView ()
		self.timer = QTimer (self)
		self.timer.timeout.connect (self.update_table)
		# self.tableView_Arhive.setModel ( self.model )
		# self.timer.timeout(self.update_table)
		self.timer.start (60 * 10)

		self._dataP1 = None
		self._dataP2 = None
		self._dataP3 = None
		self._dataP4 = None

	# self.update_table()
	# self.model.select()
	def update_table(self):
		# self.beginResetModel()
		# self.model1 = PandasModel ( dataP1 )
		self.model2 = PandasModel (dataP2)
		self._dataP4 = dataP4
		self._dataP3 = dataP3
		self._dataP1 = dataP1
		# self.model1.dataChanged.emit ( QtCore.QModelIndex (), QtCore.QModelIndex () )
		# self.model.setData(self, 1, 1)
		# self.tableView_plat_1.setModel ( self.model1 )
		self.tableView_plat_2.setModel (self.model2)
		# self.setCentralWidget(self.table)
		# self.model1.dataChanged.emit ( QtCore.QModelIndex (), QtCore.QModelIndex () )
		self.model2.dataChanged.emit (QtCore.QModelIndex (), QtCore.QModelIndex ())

		"""
		TableWidgt Окно ПМК20
		"""
		self.tableWidget.setItem (2, 0, QTableWidgetItem (str (int (dataP4[0][0]))))
		var = int (dataP4[1][1])
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

		self.tableWidget.setItem (0, 0, QTableWidgetItem (msg))  # Num ID Modbus RTU
		numVersion = str (int (dataP4[1][2]))
		self.tableWidget.setItem (0, 1, QTableWidgetItem (numVersion))  # Номер версии
		idPMK = str (hex (int (dataP4[1][3])))
		self.tableWidget.setItem (0, 2, QTableWidgetItem (idPMK))  # Номер шасси ПМК

		idPi1 = (str (hex (int (dataP4[1][4]))) + ' ' +
				 str (hex (int (dataP4[1][5]))) + ' ' +
				 str (hex (int (dataP4[1][6]))) + ' ' +
				 str (hex (int (dataP4[1][7]))) + ' ' +
				 str (hex (int (dataP4[1][8]))) + ' ' +
				 str (hex (int (dataP4[1][9]))))

		self.tableWidget.setItem (0, 3, QTableWidgetItem (idPi1))  # Номер платы измерения 1

		md5 = (str (hex (int (dataP4[2][0]))) + ' ' +
			   str (hex (int (dataP4[2][1]))) + ' ' +
			   str (hex (int (dataP4[2][2]))) + ' ' +
			   str (hex (int (dataP4[2][3]))) + ' ' +
			   str (hex (int (dataP4[2][4]))) + ' ' +
			   str (hex (int (dataP4[2][5]))) + ' ' +
			   str (hex (int (dataP4[2][6]))) + ' ' +
			   str (hex (int (dataP4[2][7]))))

		self.tableWidget.setItem (0, 5, QTableWidgetItem (md5))  # Номер платы измерения 1

		"""""
		tblitems_1 окно Плата 1
		"""
		for i in range(10):
			modeCh1ch = str(int(dataP1[0][i]))
			self.tblitems_1.setItem(1, i, QTableWidgetItem (modeCh1ch)) # режим работы канала платы 1
			self.tblitems_1.item(1, i).setTextAlignment (Qt.AlignVCenter | Qt.AlignHCenter)
		for i in range (10):
			deltaAlarm1ch = str(int(dataP1[1][i]))+' %'
			self.tblitems_1.setItem(3, i, QTableWidgetItem (deltaAlarm1ch))  # допустимое авар. отклонение сопр. изоляции 1
			self.tblitems_1.item(3, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
		for i in range (10):
			deltaAlarm1ch = str(int(dataP1[2][i]))+' %'
			self.tblitems_1.setItem(4, i, QTableWidgetItem (deltaAlarm1ch))  # допустимое авар. отклонение сопр. шлеййфа 1
			self.tblitems_1.item(4, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
		for i in range (10):
			deltaWorn1ch = str(int(dataP1[3][i]))+' %'
			self.tblitems_1.setItem(5, i, QTableWidgetItem (deltaWorn1ch))  # допустимое прдедупр. отклонение сопр. изоляции 1
			self.tblitems_1.item(5, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
		for i in range (10):
			deltaWorn1ch = str(int(dataP1[4][i]))+' %'
			self.tblitems_1.setItem(6, i, QTableWidgetItem (deltaWorn1ch))  # допустимое предупр. отклонение сопр. шлеййфа 1
			self.tblitems_1.item(6, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
		for i in range (10):
			setUch1 = str(int(dataP1[5][i])) #+' В'
			self.tblitems_1.setItem(8, i, QTableWidgetItem (setUch1))  # допустимое значение напряжения на входе
			self.tblitems_1.item(8, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
		for i in range (10):
			setRZ1 = str(dataP1[6][i]) #+' MОм'
			self.tblitems_1.setItem(9, i, QTableWidgetItem (setRZ1))  # уставка сопр. изоляции 1
			self.tblitems_1.item(9, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
		for i in range (10):
			setRZ2 = str (dataP1[7][i]) #+ ' MОм'
			self.tblitems_1.setItem (10, i, QTableWidgetItem (setRZ2))  # уставка сопр. изоляции 2
			self.tblitems_1.item (10, i).setTextAlignment (Qt.AlignVCenter | Qt.AlignHCenter)
		for i in range (10):
			setRloop = str (dataP1[8][i]) #+ ' кОм'
			self.tblitems_1.setItem(11, i, QTableWidgetItem (setRloop))  # уставка сопр. шлеййфа
			self.tblitems_1.item (11, i).setTextAlignment (Qt.AlignVCenter | Qt.AlignHCenter)
		for i in range (10):
			RZ1 = str(dataP1[9][i]) #+' MОм'
			self.tblitems_1.setItem(13, i, QTableWidgetItem(RZ1))  # Cопр. изоляции 1
			self.tblitems_1.item(13, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
		for i in range (10):
			RZ2 = str(dataP1[10][i]) #+' MОм'
			self.tblitems_1.setItem(14, i, QTableWidgetItem(RZ2))  # Cопр. изоляции 2
			self.tblitems_1.item(14, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
		for i in range (10):
			Rloop = str (dataP1[11][i])# + ' кОм'
			self.tblitems_1.setItem(15, i, QTableWidgetItem(Rloop))  # Сопр. шлеййфа
			self.tblitems_1.item (15, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
		for i in range (10):
			Uin1 = str(int(dataP1[12][i])) #+' В'
			self.tblitems_1.setItem(16, i, QTableWidgetItem(Uin1))  # значение напряжения на входе1
			self.tblitems_1.item(16, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
		for i in range (10):
			Uin2 = str(int(dataP1[13][i])) #+' В'
			self.tblitems_1.setItem(17, i, QTableWidgetItem(Uin2))  # значение напряжения на входе1
			self.tblitems_1.item(17, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
		for i in range(10):
			for i in range(10):
				AlarmRz1 = int(dataP1[14][i])
				if AlarmRz1 == 2:
					self.tblitems_1.setItem(20, i, QTableWidgetItem('A'))  # значение напряжения на входе1
					self.tblitems_1.item(20, i).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
					self.tblitems_1.item (20, i).setBackground (QtGui.QColor (255, 0, 0))  # Красный
					self.tblitems_1.item (20, i,).setForeground(QtGui.QColor (255, 255, 255))
				elif AlarmRz1 == 1:
					self.tblitems_1.setItem (20, i, QTableWidgetItem ('П'))  # значение напряжения на входе1
					self.tblitems_1.item (20, i).setTextAlignment (Qt.AlignVCenter | Qt.AlignHCenter)
					self.tblitems_1.item (20, i).setBackground (QtGui.QColor (255, 255, 0))  # желтый
				else:
					self.tblitems_1.setItem (20, i, QTableWidgetItem ('Норма'))  # значение напряжения на входе1
					self.tblitems_1.item (20, i).setTextAlignment (Qt.AlignVCenter | Qt.AlignHCenter)


	# self.tableWidget.setItem (1, 1, QTableWidgetItem ("УКККФ"))		#(dataP4[0][0]))
	# self.table.close()
	# self.table.show()
	# self.endResetModel()
	# self.tableView.setModel(PandasModel)
	# time.sleep(5)

	def defAddMb(self):
		# self.lineEdit_1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)

		tCombo1 = int (self.comboBox_1.currentText (), 16)
		tCombo2 = int (self.comboBox_2.currentText (), 16)
		intCombo = tCombo1 * 16 + tCombo2
		# dat.set_id_serial (intCombo)
		print ('ВВеден номер = ', intCombo)
		dataP4[0][0] = intCombo

		self.label_info.setText (str (hex (intCombo)))
	# self.tblitems_2.setItem (1, 1, QTableWidgetItem ("Ура!!!!!", ))


# endregion
data = np.array ([
	[1, 9, 2],
	[1, 0, -1],
	[3, 5, 2],
	[3, 3, 2],
	[5, 8, 9],
])


# region Task(array)
# task executed in a child process
def task(array):
	# create a new numpy array backed by the raw array
	dataAll = frombuffer (array, dtype = double, count = len (array))
	# reshape array into preferred shape
	dataAll = dataAll.reshape ((26, 40))
	dataSumm = np.hsplit (dataAll, 4)
	dataP1 = dataSumm[0]
	dataP2 = dataSumm[1]
	dataP3 = dataSumm[2]
	dataP4 = dataSumm[3]
	# check the contents
	print (f'Child\n{dataP2}')

	mB = myModbus ()
	# increment the data
	while (True):
		# dataP1[:] += 1
		# dataP1[1][1] = str ( 300 )
		# dataP2[:] += 20
		# confirm change
		print (f'Child\n{dataP4}')
		time.sleep (1)
		print ('P4 00 = ', dataP4[0][0])
		mB.setDataP1 (dataP1)
		mB.setDataP2 (dataP2)
		mB.setDataP3 (dataP3)
		mB.setDataP4 (dataP4)
		mB.con ()
		mB.getDataP1 ()
		mB.getDataP2 ()
		mB.getDataP3 ()
		mB.getDataP4 ()


# endregion

# region Visu(array)
def visu(array):
	dataAll = frombuffer (array, dtype = double, count = len (array))
	# reshape array into preferred shape
	dataAll = dataAll.reshape ((26, 40))
	dataSumm = np.hsplit (dataAll, 4)
	# while(True):
	dataP1 = dataSumm[0]
	dataP2 = dataSumm[1]
	dataP3 = dataSumm[2]
	dataP4 = dataSumm[3]

	# dataP1[1][2] = 25
	# dataP2[1][2] = 500 + 1
	app = QApplication (sys.argv)
	window = MainWindow ()
	window.show ()
	window.update_table ()
	# time.sleep(1)
	app.exec ()


# endregion
# protect the entry point
if 1 == 1:
	# define the size of the numpy array
	n = 26 * 40
	# create the shared array
	array = RawArray ('d', n)
	# create a new numpy array backed by the raw array

	dataAll = frombuffer (array, dtype = double, count = len (array))

	# reshape array into preferred shape
	dataAll = dataAll.reshape (26, 40)
	# populate the array
	dataAll.fill (1.0)
	dataSumm = np.hsplit (dataAll, 4)
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

	dataP2 = pd.DataFrame (dataP2,
		columns = ['Калал 1', 'Калал 2', 'Калал 3', 'Калал 4', 'Калал 5',
				   'Калал 6', 'Калал 7', 'Калал 8', 'Калал 9', 'Калал 10'],
		index = ['Режим работы:', 'Режим работы канала', 'Допустимые диапазоны:',
				 'Диапазон сопр. изоляции авар.',
				 'Диапазон сопр. шлейфа авар.', 'Диапазон сопр. изоляции предупр.',
				 'Диапазон сопр. шлейфа предупр.',
				 'Уставки:', 'Уставка напряжения на входе', 'Уставка сопр. изоляции 1',
				 'Уставка сопр. изоляции 2',
				 'Уставка сопр. шлейфа', 'Текущие значения:', 'Сопр. изоляции 1', 'Сопр. изоляции 1',
				 'Сопр. шлейфа', 'Напряжение на входе 1', 'Напряжение на входе 2',
				 'Расчетное знач. объем. наряжение', 'Авария - "А", предупрежд. - "П"',
				 'Сопр. изоляции 1 ниже доп.',
				 'Сопр. изоляции 2 ниже доп.', 'Сопр. шлейфа ниже доп.', 'Сопр. шлейфа выше доп.',
				 'Напряжение на входе 1 выше доп.', 'Напряжение на входе 2 выше доп.'])

	# confirm contents of the new array
	print (f'Parent\n{data}')
	# create a child process
	child1 = Process (target = task, args = (array,), daemon = True)
	child2 = Process (target = visu, args = (array,), daemon = True)
	# start the child process
	child2.start ()
	child1.start ()
	# wait for the child process to complete
	child2.join ()
	# check some data in the shared array

	print (f'Parent\n{data}')
