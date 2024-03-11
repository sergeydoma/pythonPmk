import minimalmodbus


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



	def con(self):

		try:
			instrument = minimalmodbus.Instrument('/dev/ttyUSB0', int(self._dataP4[0][0]))
			instrument.serial.baudrate = 9600
			instrument.serial.timeout = 1.0
			instrument.mode = minimalmodbus.MODE_RTU

			# instrument.close_port_after_each_call = True
		except IOError:
			print("Ошибка подключения по RS-485_2")
			instrument.close_port_after_each_call = True
			# instrument.serial.close()
		else:
			print("Подключение по RS - 485 выполнено")
			try:
				alarmRz1 = instrument.read_bits(registeraddress=20, number_of_bits=10)

			# 	self.dat.set_alarm_riz1(alarmRz1)
			# 	warnRz1 = instrument.read_bits(registeraddress=110, number_of_bits=10)
			# 	self.dat.set_warning_riz1(warnRz1)
			#
			# 	alarmRz2 = instrument.read_bits(registeraddress=30, number_of_bits=10)
			# 	self.dat.set_alarm_riz2(alarmRz2)
			# 	warnRz2 = instrument.read_bits(registeraddress=120, number_of_bits=10)
			# 	self.dat.set_alarm_riz2(warnRz2)
			#
			# 	alarmLoop = instrument.read_bits(registeraddress=40, number_of_bits=10)
			# 	self.dat.set_alarm_loop(alarmLoop)
			# 	warnLoop = instrument.read_bits(registeraddress=130, number_of_bits=10)
			# 	self.dat.set_warning_loop(warnLoop)
			#
			# 	alarmU = instrument.read_bits(registeraddress=100, number_of_bits=10)
			# 	self.dat.set_alarmU(alarmU)
			# 	'''
			# 	Аналоговые сигналы
			# 	'''
			# 	delta_Alarm = instrument.read_registers(registeraddress=0,number_of_registers=10)
			# 	self.dat.set_delta_alarm(delta_Alarm)
			#
			# 	delta_Warning = instrument.read_registers(registeraddress=250, number_of_registers=10)
			# 	self.dat.set_delta_warning(delta_Warning)
			#
			# 	point_rz1 = instrument.read_registers(registeraddress=10, number_of_registers=10)
			# 	self.dat.set_point_rz1(point_rz1)
			#
			# 	point_rz2 = instrument.read_registers(registeraddress=20, number_of_registers=10)
			# 	self.dat.set_point_rz2(point_rz2)
			#
			# 	point_loop = instrument.read_registers(registeraddress=30, number_of_registers=10)
			# 	self.dat.set_point_loop(point_loop)
			#
			# 	point_u = instrument.read_registers(registeraddress=200, number_of_registers=10)
			# 	self.dat.set_point_u(point_u)
			#
			# 	mode_chanal = instrument.read_registers(registeraddress=40, number_of_registers=10)
			# 	self.dat.set_mode_chanel(mode_chanal)
				for i in range (10):
					Rz1 = instrument.read_registers(registeraddress=(50+i), number_of_registers=1)
					self._dataP1[2][i] = Rz1
			#
			# 	rz2 = instrument.read_registers(registeraddress=60, number_of_registers=10)
			# 	self.dat.set_rz2(rz2)
			#
			# 	rloop = instrument.read_registers(registeraddress=70, number_of_registers=10)
			# 	self.dat.set_rloop(rloop)
			#
			# 	u1 = instrument.read_registers(registeraddress=190, number_of_registers=10)
			# 	self.dat.set_u1(u1)
			#
			# 	u2 = instrument.read_registers(registeraddress=230, number_of_registers=10)
			# 	self.dat.set_u2(u2)
			#
			#
			# 		# instrument.serial.close()
			#
			except IOError:
				print("нет связи с устройсвом по адресу", str(self._dataP4[0][0]))
			# 	# instrument.serial.close()
			# 	time.sleep(5)
				instrument.close_port_after_each_call = True
			else:
				print ("Подключение по Modbus RTU выполнено")
				print ('RZ1 = ', alarmRz1)
				instrument.close_port_after_each_call = True

