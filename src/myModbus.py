import ctypes
import time

import minimalmodbus
from dns import serial
from msrest.pipeline import requests
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

			print("Подключение по RS - 485 выполнено")
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

				print('NVERSION = ', self._dataP4[1][2])
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
				print('Rp1', Rdp1)
				print('Rm1', Rdm1)
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
				print('Rp2', Rdp2)
				print('Rm2', Rdm2)
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

				print("alarm rz1", self._dataP1[14][0])
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
				print("U1 =", U1_alarm)
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
			print("Подключение по RS - 485 выполнено")
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

				print('NVERSION = ', self._dataP4[1][2])
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
				print('Rp1', Rdp1)
				print('Rm1', Rdm1)
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

				print('Rp2', Rdp2)
				print('Rm2', Rdm2)
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

				print("alarm rz1", self._dataP1[14][0])
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
				print("U1 =", U1_alarm)
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


