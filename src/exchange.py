import multiprocessing
import minimalmodbus

import time
import psycopg2
from psycopg2 import Error
class data_exchange:
    """
    data_exchange:
    """

    __alarm_riz1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    __warning_riz1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    __alarm_riz2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    __warnig_riz2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    __alarm_loop = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    __warning_loop = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    __alarmU = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    __delta_Alarm = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    __delta_Warning = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    __point_rz1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    __point_rz2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    __point_loop = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    __point_u = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    __mode_chanel = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    __rz1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    __rz2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    __rloop = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    __u1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    __u2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    __mode_device = 0
    __id_serial = [0]
    __message = ''
    # def __init__(cls):
        # cls.__alarm_riz1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # self.__warning_riz1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # self.__alarm_riz2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # self.__warnig_riz2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # self.__alarm_loop = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # self.__warning_loop = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # self.__alarmU = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        #
        # self.__delta_Alarm = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # self.__delta_Warning = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # self.__point_rz1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # self.__point_rz2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # self.__point_loop = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # self.__point_u = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # self.__mode_chanel = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # self.__rz1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # self.__rz2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # self.__rloop = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # self.__u1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # self.__u2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # self.__mode_device = 0
        # self.__id_serial = [0]
        # self.__message = ''

        #Выберите номер устройства на шине Modbus RTU \n и нажмите кнопку "Подключить"
    """
    Сопротивление изоляции 1 выше заданного аварийного значения boolArr 20 ... 29
    """
    @classmethod
    def get_alarm_riz1(cls):
        return cls.__alarm_riz1

    @classmethod
    def set_alarm_riz1(cls, ariz1):
        cls.__alarm_riz1 = ariz1
    """
    Сопротивление изоляции 1 выше заданного предупредительного значения boolArr 110 ... 119
    """

    @classmethod
    def get_warning_riz1(cls
):
        return cls.__warning_riz1

    @classmethod
    def set_warning_riz1(cls
, wriz1):
        cls.__warning_riz1 = wriz1
    """
    Сопротивление изоляции 2 выше заданного аварийного значения boolArr 30 ... 31
    """

    @classmethod
    def get_alarm_riz2(cls):
        return cls.__alarm_riz2

    @classmethod
    def set_alarm_riz2(cls
, ariz2):
        cls.__alarm_riz2 = ariz2
    """
    Сопротивление изоляции 2 выше заданного предупредительного значения boolArr 120 ... 129
    """

    @classmethod
    def get_warning_riz2(cls):
        return cls.__warning_riz2

    @classmethod
    def set_warning_riz2(cls, wriz2):
        cls.__warning_riz2 = wriz2
    """
    Сопротивление изоляции шлейфа выше заданного аварийного значения boolArr 140 ... 149
    """

    @classmethod
    def get_alarm_loop(cls):
        return cls.__alarm_loop

    @classmethod
    def set_alarm_loop(cls
, aloop):
        cls.__alarm_loop = aloop
    """
    Сопротивление изоляции шлейфа выше заданного аварийного значения boolArr 140 ... 149
    """

    @classmethod
    def get_warning_loop(cls):
        return cls.__warning_loop

    @classmethod
    def set_warning_loop(cls, wloop):
        cls.__warning_loop = wloop

    """
    Постоянная состовляющая напряжения в измеряемом кабеле выше допустимого занчения boolArr 100 ... 109
    """

    @classmethod
    def get_alarmU(cls):
        return cls.__alarmU

    @classmethod
    def set_alarmU(cls, aU):
        cls.__alarmU = aU

    """
    Допустимое  аварийное отклонение значений сопротивлений wordArr 0 ... 9
    """

    @classmethod
    def get_delta_alarm(cls):
        return cls.__delta_Alarm

    @classmethod
    def set_delta_alarm(cls, adelta):
        cls.__delta_Alarm = adelta
    """
    Допустимое  предупредительное отклонение значений сопротивлений wordArr 250 ... 259
    """

    @classmethod
    def get_delta_warning(cls):
        return cls.__delta_Warning

    @classmethod
    def set_delta_warning(cls, wdelta):
        cls.__delta_Warning = wdelta

    """
    Уставка сопротивления изоляции 1 wordArr 10 ... 19
    """

    @classmethod
    def get_point_rz1(cls):
        return cls.__point_rz1

    @classmethod
    def set_point_rz1(cls, prz1):
        cls.__point_rz1 = prz1

    """
    Уставка сопротивления изоляции 2 wordArr 20 ... 29
    """

    @classmethod
    def get_point_rz2(cls):
        return cls.__point_rz2

    @classmethod
    def set_point_rz2(cls, prz2):
        cls.__point_rz1 = prz2

    """
    Уставка сопротивления шлейфа 30 ... 39
    """

    @classmethod
    def get_point_loop(cls):
        return cls.__point_loop

    @classmethod
    def set_point_loop(cls, ploop):
        cls.__point_loop = ploop

    """
   Уставка уставки постоянной состовляющей напряжения в измеряемом кабеле  200 ... 209
   """

    @classmethod
    def get_point_u(cls):
        return cls.__point_u

    @classmethod
    def set_point_u(cls, pu):
        cls.__point_u = pu
    """
    Режим работы канала 40 ... 49
    """

    @classmethod
    def get_mode_chanel(cls):
        return cls.__mode_chanel

    @classmethod
    def set_mode_chanel(cls, modeC):
        cls.__mode_chanel = modeC
    """
    Текущие значения сопротивления изоляции 1  50 ... 59
    """

    @classmethod
    def get_rz1(cls):
        return cls.__rz1

    @classmethod
    def set_rz1(cls, rz1):
        cls.__rz1 = rz1

    """
    Текущие значения сопротивления изоляции 2  60 ... 69
    """

    @classmethod
    def get_rz2(cls):
        return cls.__rz2

    @classmethod
    def set_rz2(cls, rz2):
        cls.__rz2 = rz2
    """
    Текущие значения сопротивления шлейфа 70 ... 79
    """

    @classmethod
    def get_rloop(cls):
        return cls.__rloop

    @classmethod
    def set_rloop(cls, rloop):
        cls.__rloop = rloop

    """
    Наряжение утечки 1 190 ... 199
    """

    @classmethod
    def get_u1(cls):
        return cls.__u1

    @classmethod

    def set_u1(cls, u1):
        cls.__u1 = u1
    """
    Наряжение утечки 2 230 ... 239
    """

    @classmethod
    def get_u2(cls):
        return cls.__u2

    @classmethod
    def set_u2(cls, u2):
        cls.__u2 = u2

    """
    Режим работы устройтва 144
    """

    @classmethod
    def get_mode_device(cls):
        return cls.__mode_device

    @classmethod
    def set_mode_device(cls, mdevice):
        cls.__mode_device = mdevice

    """
    Адрес устройства на шине modbus
    """

    @classmethod
    def get_id_serial(cls):
        return cls.__id_serial

    @classmethod
    def set_id_serial(cls, id_serial):
        cls.__id_serial = id_serial

    """
    Сообщения на главном экране
    """

    @classmethod
    def get_message(cls):
        return cls.__message

    @classmethod
    def set_message(cls, message):
        cls.__message = message



dataw = data_exchange()

dataw.set_id_serial(1)
dataw.set_mode_device(0xFFFF)
print("DAT =", dataw.get_rz1())


class myModbus(data_exchange):
    def __init__(self):
        data_exchange.__init__(self)
        self.dat = data_exchange

    def get_mode(self):

        try:
            addr = self.dat.get_id_serial()
            instrument = minimalmodbus.Instrument('/dev/ttyUSB0', self.dat.get_id_serial())
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
                self.dat.set_mode_device(modeDev)


            except IOError:
                print("нет связи с устройсвом по адресу", self.dat.get_id_serial())

    def con(self):

        try:

            instrument = minimalmodbus.Instrument('/dev/ttyUSB0', self.dat.get_id_serial())

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
                self.dat.set_alarm_riz1(alarmRz1)
                warnRz1 = instrument.read_bits(registeraddress=110, number_of_bits=10)
                self.dat.set_warning_riz1(warnRz1)

                alarmRz2 = instrument.read_bits(registeraddress=30, number_of_bits=10)
                self.dat.set_alarm_riz2(alarmRz2)
                warnRz2 = instrument.read_bits(registeraddress=120, number_of_bits=10)
                self.dat.set_alarm_riz2(warnRz2)

                alarmLoop = instrument.read_bits(registeraddress=40, number_of_bits=10)
                self.dat.set_alarm_loop(alarmLoop)
                warnLoop = instrument.read_bits(registeraddress=130, number_of_bits=10)
                self.dat.set_warning_loop(warnLoop)

                alarmU = instrument.read_bits(registeraddress=100, number_of_bits=10)
                self.dat.set_alarmU(alarmU)
                '''
                Аналоговые сигналы
                '''
                delta_Alarm = instrument.read_registers(registeraddress=0,number_of_registers=10)
                self.dat.set_delta_alarm(delta_Alarm)

                delta_Warning = instrument.read_registers(registeraddress=250, number_of_registers=10)
                self.dat.set_delta_warning(delta_Warning)

                point_rz1 = instrument.read_registers(registeraddress=10, number_of_registers=10)
                self.dat.set_point_rz1(point_rz1)

                point_rz2 = instrument.read_registers(registeraddress=20, number_of_registers=10)
                self.dat.set_point_rz2(point_rz2)

                point_loop = instrument.read_registers(registeraddress=30, number_of_registers=10)
                self.dat.set_point_loop(point_loop)

                point_u = instrument.read_registers(registeraddress=200, number_of_registers=10)
                self.dat.set_point_u(point_u)

                mode_chanal = instrument.read_registers(registeraddress=40, number_of_registers=10)
                self.dat.set_mode_chanel(mode_chanal)

                rz1 = instrument.read_registers(registeraddress=50, number_of_registers=10)
                self.dat.set_rz1(rz1)

                rz2 = instrument.read_registers(registeraddress=60, number_of_registers=10)
                self.dat.set_rz2(rz2)

                rloop = instrument.read_registers(registeraddress=70, number_of_registers=10)
                self.dat.set_rloop(rloop)

                u1 = instrument.read_registers(registeraddress=190, number_of_registers=10)
                self.dat.set_u1(u1)

                u2 = instrument.read_registers(registeraddress=230, number_of_registers=10)
                self.dat.set_u2(u2)


                    # instrument.serial.close()

            except IOError:
                print("нет связи с устройсвом по адресу", dat.get_id_serial())
                # instrument.serial.close()
                time.sleep(5)


class process_mb(myModbus):

    def __init__(self):
        myModbus.__init__(self)
        self.dat = data_exchange()
        self.m_m = myModbus()



    # @classmethod

    # def exchang(self):
    #
    #     while(True):
    #     # for i in range(1, 2):
    #         self.m_m.get_mode()
    #         res = self.dat.get_mode_device()
    #         print('выход блока =', res)
    #
    #         if (self.dat.get_mode_device() != 0xF00F):
    #
    #             self.m_m.con()
    #
    #             res = self.dat.get_alarm_riz1()
    #             print('авария сопр. изляции 1 =', res)
    #             res = self.dat.get_delta_alarm()
    #             print('аварийный диапазон = ', res)
    #             res = self.dat.get_rz1()
    #             print('Сопротивление изоляции 1 = ', res)
    #         time.sleep(1)
# pmb = process_mb()
# pmb.exchang()
"""
Работа с базой данных
"""
import datetime
w = dataw.get_rz1()


class database:

    # val1 = 0
    # val2 = 0
    # val3 = 0
    # val4 = 0
    # val5 = 0
    # val6 = 0
    # val7 = 0
    # val8 = 0
    # val9 = 0
    # val10 = 0
    def load_Rz1(self, value):

        self._value = value
    # print("val1 =", val1)
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

            # print('val2 = ',val2)
            # Выполнение SQL-запроса для вставки данных в таблицу
            insert_query_db = """ INSERT INTO rz1_4 (
                                    TIME            ,
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
                                    VALUES (CURRENT_TIMESTAMP, 'RZ1', %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            cursor.execute(insert_query_db, (self._value[0], self._value[1], self._value[2],
                                             self._value[3], self._value[4], self._value[5], self._value[6],
                                             self._value[7], self._value[8], self._value[9]))
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


dbc = database()

dbc.load_Rz1(value=w)

mMod = myModbus