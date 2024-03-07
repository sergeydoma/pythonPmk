#!/usr/bin/env python3
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
import tktooltip
from tktooltip import ToolTip

import minimalmodbus

import threading, time


import serial.tools.list_ports

ports = serial.tools.list_ports.comports()

for port in ports:
    print(port.device)

from multiprocessing import Process

# import name
numVer = 0  # Номер версии ПО

b = 0  # вспомогательная для платы измерения
ha_sh = "00002"  # Контрольная сумма md5
IdPmk = "00003"  # ID PMK
statusAdc = 0
status100v = 0
rins1 = 0
rins2: int=0
rloop = 0
stButton = 'disabled'
setIdpmk = 0
setwritte = 0

str_error = '-*-*-'
# Предустановки

idpmk = str_error
idPi = str_error # ID платы измерения
lbloop = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lbrins1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lbrins2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lbAdc = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lb100 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lbn = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# idPi = "Нет загруженных данных"

delta = 2  # смещение полей влево
my_font1 = ('Arial Bold', 16)
my_font2 = ('Arial Bold', 20)
my_color1: str = 'cornsilk2'
my_color2 = "#90EE90"  # "PaleGreen" #   "honeydew"  #"gold"
my_colordf = '#d9d9d9'
my_coloralarm = "red"

infocolor = "cornsilk2"
readymb = 0
set_id = 0
def Rloop(n):
    """
Функция для формирования окон сопротивления петли
    :param n:
    """
    lbloop[n] = Label(window, text=str_error, font=my_font1, borderwidth=4, relief="ridge", width=7, padx=6, pady=0,
                      height=2, bg=my_color1)
    lbloop[n].grid(column=n + delta, row=12, rowspan=1, columnspan=1, sticky=tk.W)


def Rins2(n):
    """
Сопротивление изоляции 2
    :param n:
    """
    lbrins2[n] = Label(window, text=str_error, font=my_font1, borderwidth=4, relief="ridge", width=7, padx=6, height=2,
                       bg=my_color1)
    lbrins2[n].grid(column=n + delta, row=11, rowspan=1, columnspan=1, sticky=tk.W)
def Rins1(n):
    """
Сопротивление изоляции 1
    :param n:
    """
    lbrins1[n] = Label(window, text=str_error, font=my_font1, borderwidth=4, relief="ridge", width=7, padx=6, height=2,
                       bg=my_color1)
    lbrins1[n].grid(column=n + delta, row=10, rowspan=1, columnspan=1, sticky=tk.W)


def u100v(n):
    """
наличие смещения 100 В на входе АЦП
    :param n:
    """
    lb100[n]  = Label(window, text = str_error, font = my_font1, borderwidth=4, relief="ridge" , width=7, padx=6,height=2, bg = my_color1)
    lb100[n].grid (column = n+delta, row =9, rowspan=1, columnspan =1, sticky = tk.W)

def AdcSt(n):
    """
    Состояние АЦП 1...10
  #  :param n:
    """
    lbAdc[n] = Label(window, text=str_error, font=my_font1, borderwidth=4, relief="ridge", width=7, padx=6, height=2,
                     bg=my_color1)
    lbAdc[n].grid(column=n + delta, row=8, rowspan=1, columnspan=1, sticky=tk.W)
def num(n):
    """
колонки с номерами каналов
    :param n:
    """
    lbn[n] = Label(window, text=str(n + 1), font=my_font1, borderwidth=4, relief="ridge", width=7, padx=6, height=2)
    lbn[n].grid(column=n + delta, row=7, rowspan=1, columnspan=1, sticky=tk.W)

def clear():
    """
функция очистки полей экрана
    """
    lbHash.config(text = str_error, bg=my_color1)
    lbID.config(text = str_error, bg=my_color1)
    lbnVer .config(text= str_error, bg = my_color1)
    lbIdPmk.config(text= str_error, bg = my_color1)
    bt_set_id.config(state='disabled')
    en_set_id.config(state='disabled')
    for number in range(10):
        lbAdc[number].config(text=str_error, bg=my_color1)
        lb100[number].config(text=str_error, bg=my_color1)
        lbrins1[number].config(text= str_error, bg=my_color1)
        lbrins2[number].config(text=str_error, bg=my_color1)
        lbloop[number].config(text=str_error, bg=my_color1)


def clicked1():
    """
функция обработки нажатия кнопки "Считать данные"
    """
    # addr1 = int(num_mb.get(),16)
    # noinspection PyGlobalUndefined
    global numVer, hashmd, idpmk, statusAdc, status100v, rins1, rins2, instrument, infowin, ready, infocolor, readymb, addH, rloop, stButton, setwritte, setIdpmk, my_coloralarm, my_color1, my_color2, my_colordf, my_font1, my_font2
    adderror = 0
    lbEntry.config(bg=my_color2, fg='#000')
    num_mb.config(bg=my_color2, fg='#000')
    # stButton = 'normal'
    ready = 1
    bt_set_id.config(state='normal')
    en_set_id.config(state='normal')

    try:
        addr = int(num_mb.get(), 16)  # Ввод шестнадцатеричной форме
        print(addr)
        if addr > 0xFF:
            addH = 1
            lbEntry.config(bg=my_coloralarm, fg='#ffffff')
            num_mb.config(bg=my_coloralarm, fg='#ffffff')
            lb_info.config(bg=my_coloralarm, fg='#ffffff')
            lb_info.config(text='ОШИБКА!\nЗначение адреса выше\nдопустимого')  #, bg='red', fg='#ffffff')
            ready = 0
            clear()
        else:
            addH = 0

    except ValueError:
        lbEntry.config(bg=my_coloralarm, fg='#ffffff')
        num_mb.config(bg=my_coloralarm, fg='#ffffff')
        lb_info.config(text='ОШИБКА!\nВ поле адреса введено\nне корректное значение', bg='red' , fg='#ffffff')
        ready = 0
        adderror = 1
        clear()
        #finally:

    # addr = 3

    idpi = "Нет связи"

    if adderror != 1 and addH != 1:
        lb_info.config(bg=my_color1, fg='#000')
        lb_info.config(text='Данные обновлены')
    try:
        instrument = minimalmodbus.Instrument('/dev/ttyUSB0', addr)
        instrument.serial.baudrate = 9600
        instrument.serial.timeout = 1.0
        instrument.mode = minimalmodbus.MODE_RTU


        # stButton = 'normal'
    except  IOError: #TimeoutError: #
        lb_info.config(text='ОШИБКА!\nНет подключения\nпо RS-485')
        lb_info.config(bg='red', fg='#ffffff')
        instrument.serial.close()
        # stButton = 'disabled'
        ready = 0
        clear()
    if ready ==1:
        # readymb = 1
        try:
        # считываем ID платы измерения:
            idpi = ""
            hashmd = ""
            idpmk = ""
            instrument.write_register(114, 0) # проверка возможности записи
            idpi = Plat_id(100)
            lbID.config(bg=my_color1)
            # Номер версии ПО

        except IOError:
            #idpi = " Нет связи с устройством!"
            lb_info.config(text = " ОШИБКА!\nУстройство\nпо адресу: "+ str(hex(addr)) +"\nне отвечает")
            lb_info.config(bg= my_coloralarm, fg = '#ffffff')
            readymb = 0
            # stButton = 'disabled'
            clear()
        if setwritte == 0:
            lbID.config(text=idpi)
            # Номер версии ПО
            numVer = instrument.read_long(90, 4)
            lbnVer.config(text=numVer)
            # Контрольная сумма md5
            hashmd = fhashmd(120)
            lbHash.config(text = hashmd,bg=my_color1)
            # ID Платы измерения
            idpmk = instrument.read_long(110, 4)
            lbIdPmk.config(text=hex(idpmk))
            statusAdc = instrument.read_register(220)
            status100v = instrument.read_register(221)
            # print (statusAdc)
            for number in range(10):
                if statusAdc & (1 << number):
                    lbAdc[number].config(text="Отказ\nканала", bg='red', fg='#ffffff')
            # lbAdc[number].config(bg='red', fg='#ffffff')
                else:
                    lbAdc[number].config(text="В норме", bg=my_color1, fg = '#000')
                    # lbAdc[number].config(bg=my_color1)
            for number in range(10):
                if status100v & (1 << number):
                    # lb100[number].config(text="В норме", bg='my_color1')
                    lb100[number].config(text="Отказ\nканала", bg='red', fg='#ffffff')
            # lb100[number].config(bg='my_color1')
                else:
                    # lb100[number].config(text="Отказ\n канала", bg='red', fg='#ffffff')
                    lb100[number].config(text="В норме", bg= my_color1, fg = '#000')
                    # lbAdc[number].config(bg=my_color1))
            rins1 = rz(50, 0.016)
            # if ready == 1 and readymb ==1:
            ##
            for number in range(10):
                lbrins1[number].config(text=('%.2f' % rins1[number]))
            # Сопротивление изоляции 2 адрес 60 - 69
            rins2 = rz(60, 0.016)
            for number in range(10):
                lbrins2[number].config(text='%.2f' % rins2[number])
            # Сопротивление петли адрес 70 - 79
            rloop = rz(70, 1)
            for number in range(10):
                lbloop[number].config(text=rloop[number])
        else:

            instrument.BYTEORDER_BIG = 4  # LONG=4 #BYTEORDER_BIG = 2
            # instrument.write_long(300, 0xFFFFFFFA)  # 4294967295i)
            try:
                instrument.write_long(112, setIdpmk)
                instrument.write_register(114, 1)
                for number in range(20):
                    time.sleep(1)
                    varok = instrument.read_register(114)
                    if varok == 5:
                        lb_info.config(text="Запись ID ПМК-20\nпроизведена успешно.\nПерезагрузите ПМК-20.")
                        lb_info.config(bg=my_color1, fg='#000')
                        # btn.config(state='disabled')
                        break
                    else:
                        lb_info.config(text="Запись ID ПМК-20\nне произведена.\nПроверте состояние кнопки\nразрешения записи.")
                        lb_info.config(bg=my_coloralarm, fg='#ffffff')
                    # labelcurrent.config(text= str(20 - number)
            except IOError:
                print('ошибка записи!!!!')
            finally:
                bt_set_id.config(state='disabled')
                en_set_id.config(state='disabled')
                setwritte = 0
def close_window():
    """
Функция закрытия окна по кнопке
    """
    window.destroy()


window = Tk()
window.title("ООО \"Сириус\"")
window.geometry('1400x830')

# пропорциональное свертывание окна
for i in range(12):
    window.columnconfigure(i, weight=1, minsize=100)    #75)
for i in range(14):
    window.rowconfigure(i, weight=1, minsize= 60)  #50)

window.attributes('-type', True)

lbID = Label(window, text=str(idPi), font=my_font1, width=43, height=2, bg=my_color1, borderwidth=4, relief="ridge")

lbID.grid(column=2, row=3, rowspan=1, columnspan=5, sticky=tk.W)

lb3 = Label(window, text="ID паты \n измерения", font=my_font1, borderwidth=4, relief="ridge", width=14, padx=6,
            height=2)  # ,bg = my_color1)
lb3.grid(column=0, row=3, rowspan=1, columnspan=2, sticky=tk.W)

lbNpo = Label(window, text="Номер \n ПО", font=my_font1, borderwidth=4, relief="ridge", width=14, padx=6,
              height=2)  # ,bg = my_color1)
lbNpo.grid(column=0, row=4, rowspan=1, columnspan=2, sticky=tk.W)

lbnVer = Label(window, text=str_error, font=my_font1, borderwidth=4, relief="ridge", width=14, padx=6, height=2,
               bg=my_color1)
lbnVer.grid(column=2, row=4, rowspan=1, columnspan=2, sticky=tk.W)

lbmd5 = Label(window, text="Контрольная\nсумма md5", font=my_font1, borderwidth=4, relief="ridge", width=14, padx=6,
              height=2)  # ,bg = my_color1)
lbmd5.grid(column=0, row=5, rowspan=1, columnspan=2, sticky=tk.W)

lbHash = Label(window, text=str_error, font=my_font1, borderwidth=4, relief="ridge", width=42, padx=2,
               height=2, bg=my_color1)#, bg = my_color1)



lbHash.grid(column=2, row=5, rowspan=1, columnspan=8, sticky=tk.W)

lbPmk = Label(window, text="ID ПМК-20", font=my_font1, borderwidth=4, relief="ridge", width=14, padx=6,
              height=2)  # ,bg = my_color1)
lbPmk.grid(column=0, row=6, rowspan=1, columnspan=2, sticky=tk.W)

lbIdPmk = Label(window, text=str_error, font=my_font1, borderwidth=4, relief="ridge", width=14, padx=6, height=2,
                bg=my_color1)
lbIdPmk.grid(column=2, row=6, rowspan=1, columnspan=2, sticky=tk.W)

btn = Button(window, text="Считать \n данные", command=clicked1, font=my_font1, borderwidth=4, relief="ridge",
             width=12, padx=6, height=2, bg=my_color2)

btn.grid(column=0, row=1, rowspan=1, columnspan=2, padx=1, pady=1, sticky=tk.EW)

ToolTip(btn,'Команда - считать данные с устройства')

lb2 = Label(window, text=" Прибор мониторинга кабельных линий ПМК-20 ", font=("Arial Bold", 25), borderwidth=4,
            relief="ridge", width=53)

lb2.grid(column=0, row=0, rowspan=1, columnspan=12, padx=1, pady=1, sticky=tk.EW)


#CreateToolTip(lb2, text = 'Версия программного обеспечения \nХХХХХХХХ')
ToolTip(lb2,'Программа тестирования прибора \nПМК-2 версия ПО: d413ab6a от 16.07.2023 г.')

e1 = tk.StringVar()
e2 = tk.StringVar()

lbEntry = Label(window, text="    ", bg=my_color2, borderwidth=4, relief="ridge", width=10, padx=4, height=3)

lbEntry.grid(column=2, row=2, rowspan=1, columnspan=1, padx=1, pady=1, sticky=tk.EW)

num_mb = tk.Entry(window, textvariable=e1, font=my_font2, width=3, borderwidth=4, bg=my_color2,
                  justify=CENTER)  # , width = 65) # RIGHT )    #), show ="*")

num_mb.insert(2, "3")

num_mb.grid(column=2, row=2, padx=[10, 10], sticky=tk.W)
lb_10 = Label(window, text=' Задание \nадреса modbus', font=my_font1, borderwidth=4, relief="ridge", width=14, padx=6, height=2)
lb_10.grid(column=0, row=2, rowspan=1, columnspan=2, sticky=tk.W)

lb_nK = Label(window, text=' Каналы \n измерения ', font=my_font1, borderwidth=4, relief="ridge", width=14, padx=6,
              height=2)
lb_nK.grid(column=0, row=7, rowspan=1, columnspan=2, sticky=tk.W)

lb_id = Label(window, text=' Состояние АЦП   ', font=my_font1, borderwidth=4, relief="ridge", width=14, padx=6,
              height=2)
lb_id.grid(column=0, row=8, rowspan=1, columnspan=2, sticky=tk.W)

lb_100v = Label(window, text=' Напряжение \n смещения 100 В ', font=my_font1, borderwidth=4, relief="ridge", width=14,
                padx=6, height=2)
lb_100v.grid(column=0, row=9, rowspan=1, columnspan=2, sticky=tk.W)

lb_Rins1 = Label(window, text=' Сопротивление \n изоляции 1 (мОм)', font=my_font1, borderwidth=4, relief="ridge", width=14,
                 padx=6, height=2)
lb_Rins1.grid(column=0, row=10, rowspan=1, columnspan=2, sticky=tk.W)

lb_Rins2 = Label(window, text=' Сопротивление \n изоляции 2 (мОм)', font=my_font1, borderwidth=4, relief="ridge", width=14,
                 padx=6, height=2)
lb_Rins2.grid(column=0, row=11, rowspan=1, columnspan=2, sticky=tk.W)

lb_RloopZ = Label(window, text=' Сопротивление \n шлейфа (кОм) ', font=my_font1, borderwidth=4, relief="ridge",
                  width=14, padx=6, height=2)
lb_RloopZ.grid(column=0, row=12, rowspan=1, columnspan=2, sticky=tk.W)

def clicked2():
    """
 Задание ID PMK-20
    """
    global setwritte

    setwritte = 1
    error_idp = 0
    global  setIdpmk, lb_info, lbf_set_id
    try:
        setIdpmk = int(en_set_id.get(), 16)
        if setIdpmk > 0xFFFFFFFF:
            print("error")
            lbf_set_id.config(bg=my_coloralarm, fg='#ffffff')
            en_set_id.config(bg=my_coloralarm, fg='#ffffff')
            lb_info.config(bg=my_coloralarm, fg='#ffffff')
            lb_info.config(text='ОШИБКА!\nЗначение ID ПМК содержит \nизбыточное количество символов')
            error_idp = 1
    except ValueError:
        print ("error")
        lbf_set_id.config(bg=my_coloralarm, fg='#ffffff')
        en_set_id.config(bg=my_coloralarm, fg='#ffffff')
        lb_info.config(bg=my_coloralarm, fg='#ffffff')
        lb_info.config(text='ОШИБКА!\nЗначение ID ПМК содержит \nне допустимые символы')
        error_idp = 1
    # clicked1()
    if error_idp == 0:
        lbf_set_id.config(bg=my_color2, fg='#000')
        en_set_id.config(bg=my_color2, fg='#000')
        lb_info.config(bg=my_color1, fg='#000')
        # lb_info.config(text='Значение ID ПМК загружено')
        # time.sleep(15)
        # lb_info.config(text="Производится запись ID ПМК-20")  # \n произведена успешно.\nПерезагрузите ПМК-20.")
        # lb_info.config(bg='#00FF00', fg='#000')

        varok = instrument.read_register(114)
        if varok != 5:
            clicked1()
        else:
            lb_info.config(text="Для записи ID\nнужно перезагрузить ПМК-20")  # \n произведена успешно.\nПерезагрузите ПМК-20.")
            lb_info.config(bg='#FFFF00', fg='#000')
            setwritte=0
        # instrument.write_long(300, 0xFFFFFFFA)  # 4294967295i)

    print(setIdpmk)

# print ("stButton = " + str(stButton))



bt_set_id = Button(window, text="Записать \n ID ПМК-20", command = clicked2, font=my_font1, borderwidth=4, relief="ridge",
             width=12, padx=6, height=2, bg=my_color2)
#if stButton == 0:
bt_set_id.config(state = 'disabled')
ToolTip(bt_set_id, 'Команда - произвести запись идентификационного номера шасси в устройство')


bt_set_id.grid(column=5, row=6, rowspan=1, columnspan=2, sticky=tk.W)

lbf_set_id = Label(window, text='', font=my_font1, borderwidth=4, relief="ridge",
                  width=14, padx=5, height=2, bg=my_color2)
lbf_set_id.grid(column=7, row=6, rowspan=1, columnspan=2, sticky=tk.W)

en_set_id = tk.Entry(window, textvariable=e2, font=my_font2, width=10, borderwidth=4, bg=my_color2,
                  justify=CENTER)  # , width = 65) # RIGHT )    #), show ="*")
en_set_id.config(state='disabled')

en_set_id.insert(8, "0")

en_set_id.grid(column=7, row=6,columnspan=2, padx=[10, 10], sticky=tk.W)


bt_close = Button(window, text="Завершить работу \nпрограммы ", command = close_window, font=my_font1, borderwidth=4, relief="ridge",
             width=20, padx=6, height=2, bg=my_color2)
bt_close.grid(column=9, row=1, rowspan=1, columnspan=3, sticky=tk.W)


for i in range(10):
    num(i)

for i in range(10):
    u100v(i)

for i in range(10):
    AdcSt(i)

for i in range(10):
    Rins1(i)

for i in range(10):
    Rins2(i)

for i in range(10):
    Rloop(i)

# информационное окно
lb_info = Label(window, text=' Нет считанных\n данных ', font=my_font1,bg= infocolor, borderwidth=4, relief="ridge",
                  width=32, padx=4, height=4)
lb_info.grid(column=8, row=1, rowspan=4, columnspan=4, sticky=tk.W)


def fhashmd(regaddr):
    """
функция вывода значения контрольной суммы md5
    """
    md = ''
    for number in range(4):
        tempb = hex(instrument.read_long((regaddr + number * 2), 4))
        md = str(md) + " " + str(tempb)
    return md

def Plat_id(regaddr):
    """
Функция вывода id платы измерения
    :return:
    """
    idpi = ''
    for number in range(3):
        tempb = hex(instrument.read_long((regaddr + number * 2), 4))
    # instrument.write_long(300, 0xFFFFFFFA) #4294967295i)
        idpi = str(idpi) + " " + str(tempb)
    return idpi

def rz(regadd, k):
    """
   функция измерения сопротивления
    """
    rmeas = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for number in range(10):
        rmeas[number] = (instrument.read_register (regadd + number)*k)
    return rmeas

# def status(regadd):
#     stat = ''
#     out = ''
#     stat = instrument.read_register(regadd)
#
#     for number in range(10):
#         if out & (1 << number):
#             lbAdc[number].config(text="Отказ\nканала")
#             lbAdc[number].config(bg='red', fg='#ffffff')
#         else:
#             lbAdc[number].config(text="В норме")
#             lbAdc[number].config(bg=my_color1)
#     for number in range(10):
#         if status100v & (1 << number):
#             lb100[number].config(text="В норме")
#             lb100[number].config(bg='my_color1')
#         else:
#             lb100[number].config(text="Отказ\nканала")
#             lb100[number].config(bg='red', fg='#ffffff')
#     #lbrins1[number].config(text=str(rins1)
# def cliced2():
#     """
#  Задание ID PMK-20
#     """
#     print("clic_id")
# задержка !!!!
#
window.mainloop()


# Информационное окно

# if __name__ == '__main__':
#    main()
