# import serial.tools.list_ports
# from pymodbus.server.sync import StartSerialServer
from pymodbus.client.sync import ModbusSerialClient as ModbusClient


# from pymodbus.transaction import ModbusRtuFramer
# import requests
# from pymodbus.pdu import ModbusRequest


# found = False
# for i in range(64):
#     try:
#         port = "/dev/ttyUSB%d" % i
#         ser = serial.Serial(port)
#         ser.close()
#         print("Найден последовательный порт: ", port)
#         found = True
#     except serial.serialutil.SerialException:
#         pass
#
# if not found:
#     print ("Последовательных портов не обнаружено")


def connect():
    try:
        # con = None
        # response = None
        # res = [0, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ,0]
        _client = ModbusClient(retries=0, method='rtu', port='/dev/ttyUSB0', baudrate=9600, stopbits=1, parity='N',
                               bytesize=8, timeout=1)
        # client.connect()
        con = _client.connect()
        # print(con)
        # # slave_address = 0x02
        # if _client.connect():
        #     data = _client.read_holding_registers(1, count=10, unit=0x02)
        #     ##
        #     print("data = ", data.registers)
        #     res = data.registers
        #     print ("res = ", res)
        data = _client.read_holding_registers(1, count=10, unit=0x02)
        return _client
    except Exception as e:
        print("Error while connecting client: \n" + e.__str__())


client = connect()
# print(client.read_coils(0x0001, count=1, unit=0x02))
# print(client.read_holding_registers(0, count=10, unit=0x02))
# if client.connect():
res = client.read_holding_registers(0, count=10, unit=0x02).registers
print (res)
client.close()
# print (client)
