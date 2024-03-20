import datetime
import time


import psycopg2
from psycopg2 import Error

# from exchange import data_exchange as de


data_pmk = de()
w = data_pmk.get_rz1()
w1 = w[0]
w2 = w[1]
w3 = w[2]
w4 = w[3]
w5 = w[4]
w6 = w[5]
w7 = w[6]
w8 = w[7]
w9 = w[8]
w10 = w[9]


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
    # Выполнение SQL-запроса для вставки данных в таблицу

    insert_query_db = """ INSERT INTO rz1 
                            (Id             ,
                            TIME            ,
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
                            VALUES 
                            (1,
                            CURRENT_TIMESTAMP,
                            w1, w2, w3, w4, w5, w6, w7, w8, w9, w10}
                            )"""
    cursor.execute(insert_query_db)
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