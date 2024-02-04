import multiprocessing
import minimalmodbus

import time
import psycopg2
from psycopg2 import Error
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
        self.__id_serial = [0]
    """
    Сопротивление изоляции 1 выше заданного аварийного значения boolArr 20 ... 29
    """
    # @staticmethod
    def get_alarm_riz1(self):
        return self.__alarm_riz1

    # @staticmethod
    def set_alarm_riz1(self, ariz1):
        self.__alarm_riz1 = ariz1
    """
    Сопротивление изоляции 1 выше заданного предупредительного значения boolArr 110 ... 119
    """
    def get_warning_riz1(self):
        return self.__warning_riz1

    def set_warning_riz1(self, wriz1):
        self.__warning_riz1 = wriz1
    """
    Сопротивление изоляции 2 выше заданного аварийного значения boolArr 30 ... 31
    """
    def get_alarm_riz2(self):
        return self.__alarm_riz2

    def set_alarm_riz2(self, ariz2):
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

    """
    Адрес устройства на шине modbus
    """

    def get_id_serial(self):
        return self.__id_serial

    def set_id_serial(self, id_serial):
        self.__id_serial = id_serial


dat = data_exchange()
dat.set_id_serial(2)
dat.set_mode_device(0xFFFF)
print("DAT =", dat.get_rz1())

class myModbus:
    # def __init__(self, adress):
    #     self.__adress = adress



    def get_mode(self):

        try:
            addr = dat.get_id_serial()
            instrument = minimalmodbus.Instrument('/dev/ttyUSB0', dat.get_id_serial())
            instrument.serial.baudrate = 9600
            instrument.serial.timeout = 1.0
            instrument.mode = minimalmodbus.MODE_RTU
            instrument.close_port_after_each_call = True
        except IOError:
            print("Ошибка подключения по RS-485_1")

            # instrument.close_port_after_each_call = False
            # self.instrument.serial.close()
        else:
            try:
                modeDev = instrument.read_register(144, 0)
                dat.set_mode_device(modeDev)


            except IOError:
                print("нет связи с устройсвом по адресу", dat.get_id_serial())

    def con(self):



        try:

            instrument = minimalmodbus.Instrument('/dev/ttyUSB0', dat.get_id_serial())

            instrument.serial.baudrate = 9600
            instrument.serial.timeout = 1.0
            instrument.mode = minimalmodbus.MODE_RTU

            instrument.close_port_after_each_call = True
        except IOError:
            print("Ошибка подключения по RS-485_2")

            # instrument.serial.close()
        else:
            try:
                alarmRz1 = instrument.read_bits(registeraddress=20, number_of_bits=10)
                dat.set_alarm_riz1(alarmRz1)
                warnRz1 = instrument.read_bits(registeraddress=110, number_of_bits=10)
                dat.set_warning_riz1(warnRz1)

                alarmRz2 = instrument.read_bits(registeraddress=30, number_of_bits=10)
                dat.set_alarm_riz2(alarmRz2)
                warnRz2 = instrument.read_bits(registeraddress=120, number_of_bits=10)
                dat.set_alarm_riz2(warnRz2)

                alarmLoop = instrument.read_bits(registeraddress=40, number_of_bits=10)
                dat.set_alarm_loop(alarmLoop)
                warnLoop = instrument.read_bits(registeraddress=130, number_of_bits=10)
                dat.set_warning_loop(warnLoop)

                alarmU = instrument.read_bits(registeraddress=100, number_of_bits=10)
                dat.set_alarmU(alarmU)
                '''
                Аналоговые сигналы
                '''
                delta_Alarm = instrument.read_registers(registeraddress=0,number_of_registers=10)
                dat.set_delta_alarm(delta_Alarm)

                delta_Warning = instrument.read_registers(registeraddress=250, number_of_registers=10)
                dat.set_delta_warning(delta_Warning)

                point_rz1 = instrument.read_registers(registeraddress=10, number_of_registers=10)
                dat.set_point_rz1(point_rz1)

                point_rz2 = instrument.read_registers(registeraddress=20, number_of_registers=10)
                dat.set_point_rz2(point_rz2)

                point_loop = instrument.read_registers(registeraddress=30, number_of_registers=10)
                dat.set_point_loop(point_loop)

                point_u = instrument.read_registers(registeraddress=200, number_of_registers=10)
                dat.set_point_u(point_u)

                mode_chanal = instrument.read_registers(registeraddress=40, number_of_registers=10)
                dat.set_mode_chanel(mode_chanal)

                rz1 = instrument.read_registers(registeraddress=50, number_of_registers=10)
                dat.set_rz1(rz1)

                rz2 = instrument.read_registers(registeraddress=60, number_of_registers=10)
                dat.set_rz2(rz2)

                rloop = instrument.read_registers(registeraddress=70, number_of_registers=10)
                dat.set_rloop(rloop)

                u1 = instrument.read_registers(registeraddress=190, number_of_registers=10)
                dat.set_u1(u1)

                u2 = instrument.read_registers(registeraddress=230, number_of_registers=10)
                dat.set_u2(u2)


                # instrument.serial.close()

            except IOError:
                print("нет связи с устройсвом по адресу", dat.get_id_serial())
                # instrument.serial.close()
                time.sleep(5)

class process_mb:
    # def __init__(self, adress, baudrate):
    @staticmethod
    def exchang():

        # while(True):
        for i in range (1,2):

            m_m = myModbus()
            m_m.get_mode()
            res = dat.get_mode_device()
            print('выход блока =', res)

            if (dat.get_mode_device() == 0xFFFF):

                m_m.con()
                res = dat.get_alarm_riz1()
                print('авария сопр. изляции 1 =', res)
                res = dat.get_delta_alarm()
                print('аварийный диапазон = ', res)
                res = dat.get_rz1()
                print('Сопротивление изоляции 1 = ', res)
            time.sleep(3)
pmb = process_mb()
pmb.exchang()
"""
Работа с базой данных
"""
import datetime
w = dat.get_rz1()

val1 = w[0]
val2 = w[1]
val3 = w[2]
val4 = w[3]
val5 = w[4]
val6 = w[5]
val7 = w[6]
val8 = w[7]
val9 = w[8]
val10 = w[9]

print("val1 =", val1)
try:
    t = str(time.time())
    print(t)
    t = '2014-04-04 20:00:00'
    # Подключиться к существующей базе данных
    connection = psycopg2.connect(user="postgres",
                                  # пароль, который указали при установке PostgreSQL
                                  password="123",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="postgres_db")



    cursor = connection.cursor()

    print('val2 = ',val2)
    # Выполнение SQL-запроса для вставки данных в таблицу
    insert_query_db = """ INSERT INTO rz1_3 (
                            SS              ,
                            CHANAL_1        ,
                            CHANAL_2        ,
                            CHANAL_3        ,
                            CHANAL_4        ,
                            CHANAL_5        ,
                            CHANAL_6        ,
                            CHANAL_7        ,
                            CHANAL_8        ,
                            CHANAL_9        ,
                            CHANAL_10
                                )
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    cursor.execute(insert_query_db, (val1, val1, val2, val3, val4, val5, val6, val7, val8, val9, val10))
    connection.commit()
    print("1 запись успешно вставлена")
    # Получить результат
    cursor.execute("SELECT * from pmk")
    record = cursor.fetchall()
    print("Результат", record)

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")

