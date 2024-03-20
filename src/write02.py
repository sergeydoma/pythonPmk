import datetime
import time


import psycopg2
from psycopg2 import Error

from exchange import data_exchange as de

class load_rz1:
    data_pmk = de()
    w = data_pmk.get_rz1()
    idPMK = str(101) #w[0]
    NumPlat = str (222)
    NumCh = str(2)   #w[1]
    Uinput1 = str(3)    #  w[2]
    Uinput2 = str(4) #  w[3]
    RZ1 = str(5) #w[4]
    RZ2 = str(6)#w[5]
    Rloop = str(7)
    Uvol = str(8)
    # val9 = str(9)
    # val10 = str(10)



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
                                      database="pmk20_db")

        cursor = connection.cursor()
        # print('val2 = ',val2)
        # Выполнение SQL-запроса для вставки данных в таблицу
        insert_query_db = """ INSERT INTO pmk_23 (                           
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

        # # Выполнение SQL-запроса для обновления таблицы
        # update_query = """Update pmk set price = 1500 where id = 1"""
        # cursor.execute(update_query)
        # connection.commit()
        # count = cursor.rowcount
        # print(count, "Запись успешно удалена")
        # # Получить результат
        # cursor.execute("SELECT * from mobile")
        # print("Результат", cursor.fetchall())
        #
        # # Выполнение SQL-запроса для удаления таблицы
        # delete_query = """Delete from mobile where id = 1"""
        # cursor.execute(delete_query)
        # connection.commit()
        # count = cursor.rowcount
        # print(count, "Запись успешно удалена")
        # # Получить результат
        # cursor.execute("SELECT * from mobile")
        # print("Результат", cursor.fetchall())

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PostgreSQL закрыто")