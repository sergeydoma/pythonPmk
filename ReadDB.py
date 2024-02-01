import datetime
import time

import psycopg2
from psycopg2 import Error


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

    # insert_query = """ INSERT INTO pmk (TIME, MODEL, PRICE) VALUES (
    #  CURRENT_TIMESTAMP , 'Iphone12', 1100)"""
    # cursor.execute(insert_query)
    # connection.commit()
    # print("1 запись успешно вставлена")
    # # Получить результат
    # cursor.execute("SELECT * from pmk")
    # record = cursor.fetchall()
    # print("Результат", record)

    # Выполнение SQL-запроса для обновления таблицы
    update_query = """Update pmk set price = 1500 where id = 1"""
    cursor.execute(update_query)
    connection.commit()
    count = cursor.rowcount
    print(count, "Запись успешно удалена")
    # Получить результат
    cursor.execute("SELECT * from pmk")
    print("Результат", cursor.fetchall())

    # Выполнение SQL-запроса для удаления таблицы
    delete_query = """Delete from pmk where id = 2"""
    cursor.execute(delete_query)
    connection.commit()
    count = cursor.rowcount
    print(count, "Запись успешно удалена")
    # Получить результат
    cursor.execute("SELECT * from mobile")
    print("Результат", cursor.fetchall())

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")