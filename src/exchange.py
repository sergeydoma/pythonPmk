# import serial.tools.list_ports
# from pymodbus.server.sync import StartSerialServer


from pymodbus.client.sync import ModbusSerialClient as ModbusClient


class myModbus:
    """
    myModbus
    """
    # def __init__(self):


    def __init__(self):
        self.__delta_Alarm = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.__delta_Warning = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def set_delta_Alarm(self, delta):

        self.__delta_Alarm = delta

    def get_delta_Alarm(self):
        return self.__delta_Alarm


    def con(self, address, baudrate):
        global _client
        self.address = address
        self.baudrate = baudrate
        try:
            _client = ModbusClient(retries=0, method='rtu', port='/dev/ttyUSB0', baudrate=baudrate, stopbits=1, parity='N',
                                   bytesize=8, timeout=1)
            con = _client.connect()
            _client.read_coils(address, count=1, unit=0x02)
            self.__delta_Alarm = _client.read_holding_registers(0, count=10, unit=0x02).registers
            print('delta =', self.__delta_Alarm)
            return _client
            # data = _client.read_holding_registers(1, count=10, unit=0x02)
            # if _client.connect():
            #     return _client
            # else:
            #     return 'Error con'

        except Exception as e:
            print("Error while connecting client: \n" + e.__str__())


# m_m = myModbus()
# m_m.connect()

# client = m_m.con()
# if client == 'Error con':
#     raise Exception("Нет соединения с COM портом")
# print(m_m.connect())

# res = m_m.connect().read_coils(0x0001, count=1, unit=0x02).registers
# print(res)
# client = connect()
# print(client.read_coils(0x0001, count=1, unit=0x02))
# print(client.read_holding_registers(0, count=10, unit=0x02))
# if client.connect():

# res = client.read_holding_registers(1, count=10, unit=0x02).registers
# print(res)
# client.close()

# print (client)
# change
