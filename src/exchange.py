# import serial.tools.list_ports
# from pymodbus.server.sync import StartSerialServer
from time import sleep

from pymodbus.client.sync import ModbusSerialClient as ModbusClient
import sys
import time

import traceback
class data_exchange:
    """
    data_exchange:
    """
    def __init__(self):

        self.__alarm_riz1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.__warning_riz1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.__alarm_riz2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.__warnig_riz2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.__alarm_loop = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.__warning_loop = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.__alarmU = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        self.__delta_Alarm = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.__delta_Warning = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.__point_rz1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.__point_rz2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.__point_loop = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.__point_u = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.__mode_chanel = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.__rz1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.__rz2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.__rloop = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.__u1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.__u2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.__mode_device = 0
    """
    Сопротивление изоляции 1 выше заданного аварийного значения boolArr 20 ... 29
    """
    def get_alarm_riz1(self):
        return self.__alarm_riz1

    def set_a_alarm_riz1(self, ariz1):
        self.__alarm_riz1 = ariz1
    """
    Сопротивление изоляции 1 выше заданного предупредительного значения boolArr 110 ... 119
    """
    def get_warning_riz1(self):
        return self.__warning_riz1

    def set_a_warning_riz1(self, wriz1):
        self.__warning_riz1 = wriz1
    """
    Сопротивление изоляции 2 выше заданного аварийного значения boolArr 30 ... 31
    """
    def get_alarm_riz2(self):
        return self.__alarm_riz2

    def set_a_alarm_riz2(self, ariz2):
        self.__alarm_riz2 = ariz2
    """
    Сопротивление изоляции 2 выше заданного предупредительного значения boolArr 120 ... 129
    """
    def get_warning_riz2(self):
        return self.__warning_riz2

    def set_warning_riz2(self, wriz2):
        self.__warning_riz2 = wriz2
    """
    Сопротивление изоляции шлейфа выше заданного аварийного значения boolArr 140 ... 149
    """
    def get_alarm_loop(self):
        return self.__alarm_loop

    def set_alarm_loop(self, aloop):
        self.__alarm_loop = aloop
    """
    Сопротивление изоляции шлейфа выше заданного аварийного значения boolArr 140 ... 149
    """
    def get_warning_loop(self):
        return self.__warning_loop

    def set_warning_loop(self, wloop):
        self.__warning_loop = wloop

    """
    Постоянная состовляющая напряжения в измеряемом кабеле выше допустимого занчения boolArr 100 ... 109
    """
    def get_alarmU(self):
        return self.__alarmU

    def set_alarmU(self, aU):
        self.__alarmU = aU

    """
    Допустимое  аварийное отклонение значений сопротивлений wordArr 0 ... 9
    """
    def get_delta_alarm(self):
        return self.__delta_Alarm

    def set_delta_alarm(self, adelta):
        self.__delta_Alarm = adelta
    """
    Допустимое  предупредительное отклонение значений сопротивлений wordArr 250 ... 259
    """
    def get_delta_warning(self):
        return self.__delta_Warning

    def set_delta_warning(self, wdelta):
        self.__delta_Warning = wdelta

    """
    Уставка сопротивления изоляции 1 wordArr 10 ... 19
    """

    def get_point_rz1(self):
        return self.__point_rz1

    def set_point_rz1(self, prz1):
        self.__point_rz1 = prz1

    """
    Уставка сопротивления изоляции 2 wordArr 20 ... 29
    """
    def get_point_rz2(self):
        return self.__point_rz2

    def set_point_rz2(self, prz2):
        self.__point_rz1 = prz2

    """
    Уставка сопротивления шлейфа 30 ... 39
    """
    def get_point_loop(self):
        return self.__point_loop

    def set_point_loop(self, ploop):
        self.__point_loop = ploop

    """
   Уставка уставки постоянной состовляющей напряжения в измеряемом кабеле  200 ... 209
   """
    def get_point_u(self):
        return self.__point_u

    def set_point_u(self, pu):
        self.__point_u = pu
    """
    Режим работы канала 40 ... 49
    """
    def get_mode_chanel(self):
        return self.__mode_chanel

    def set_mode_chanel(self, modeC):
        self.__mode_chanel = modeC
    """
    Текущие значения сопротивления изоляции 1  50 ... 59
    """
    def get_rz1(self):
        return self.__rz1

    def set_rz1(self, rz1):
        self.__rz1 = rz1

    """
    Текущие значения сопротивления изоляции 2  60 ... 69
    """
    def get_rz2(self):
        return self.__rz2

    def set_rz2(self, rz2):
        self.__rz2 = rz2
    """
    Текущие значения сопротивления шлейфа 70 ... 79
    """
    def get_rloop(self):
        return self.__rloop

    def set_rloop(self, rloop):
        self.__rloop = rloop

    """
    Наряжение утечки 1 190 ... 199
    """
    def get_u1(self):
        return self.__u1

    def set_u1(self, u1):
        self.__u1 = u1
    """
    Наряжение утечки 2 230 ... 239
    """
    def get_u2(self):
        return self.__u2

    def set_u2(self, u2):
        self.__u2 = u2

    """
    Режим работы устройтва 144
    """
    def get_mode_device(self):
        return self.__mode_device

    def set_mode_device(self, mdevice):
        self.__mode_device = mdevice



dat = data_exchange()

# dat.set_delta_alarm([1,2,3,4,5,6,7,8,9,0])
#
# funct = dat.get_delta_alarm()
# print('funct =', funct)
class myModbus:
    """
    myModbus
    """
    # def __init__(self):


    # def __init__(self):
        # self.__delta_Alarm = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # self.__delta_Warning = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        #
        # self.__alarm_riz1 = 0
        # """
        # Сопротивление изоляции 1 выше заданного аварийного значения boolArr 20 ... 29
        # """
        # self.__warnig_riz1 = 0
        # """
        # Сопротивление изоляции 1 выше заданного предупредительного значения boolArr 110 ... 119
        # """
        # self.__alarm_riz2 = 0
        # """
        # Сопротивление изоляции 2 выше заданного аварийного значения boolArr 30 ... 31
        # """
        # self.__warnig_riz2 = 0
        # """
        # Сопротивление изоляции 2 выше заданного предупредительного значения boolArr 120 ... 121
        # """
     # dat = data_exchange()
    # def set_delta_Alarm(self, adelta):
    #     self.__delta_Alarm = adelta
    #
    #
    # def get_delta_Alarm(self):
    #     return self.__delta_Alarm

    global _client

    def get_mode(self,address, baudrate):
        self.address = address
        self.baudrate = baudrate
        try:
            _client = ModbusClient(retries=0, method='rtu', port='/dev/ttyUSB0', baudrate=baudrate, stopbits=1, parity='N',
                                   bytesize=8, timeout=1)
            ress = _client.read_holding_registers(144, count=1, unit=0x02).registers
            dat.set_mode_device(ress)

            ress1 = _client.read_discrete_inputs(20, count=10, uint=0x02).registers
            print('a', ress1)
            dat.set_a_alarm_riz1(ress1)

        except Exception as e:
            print("Error while connecting client: \n" + e.__str__())

    def con(self, address, baudrate):
        self.address = address
        self.baudrate = baudrate
        try:
            _client = ModbusClient(retries=0, method='rtu', port='/dev/ttyUSB0', baudrate=baudrate, stopbits=1, parity='N',
                                   bytesize=8, timeout=1)
            # con = _client.connect()
            # _client.read_coils(address, count=1, unit=0x02)
            # ress = _client.read_coil(144, count=1, unit=0x02).registers


            ress = _client.read_holding_registers(144, count=1, unit=0x02).registers
            dat.set_mode_device(ress)


        except Exception as e:
            print("Error while connecting client: \n" + e.__str__())

def exchang():
    # m_m = myModbus()
    # m_m.con(1, 9600)

    # client = m_m.con()
    # if client == 'Error con':


    #     raise Exception("Нет соединения с COM портом")
    # print(m_m.connect())
    while(1):
        m_m = myModbus()
        m_m.get_mode(1, 9600)
        res = dat.get_mode_device()
        print('выход блока =', res)
        res = dat.get_alarm_riz1()
        print('авания сопр. изляции 1 =', res)
        time.sleep(1)
exchang()

# client = connect()
# print(client.read_coils(0x0001, count=1, unit=0x02))
# print(client.read_holding_registers(0, count=10, unit=0x02))
# if client.connect():

# res = client.read_holding_registers(1, count=10, unit=0x02).registers
# print(res)
# client.close()

# print (client)
# change
