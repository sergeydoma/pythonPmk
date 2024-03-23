
import psycopg2
from psycopg2 import Error

try:
    # Подключиться к существующей базе данных
    connection = psycopg2.connect(user="postgres",
                                  # пароль, который указали при установке PostgreSQL
                                  password="123",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="pmk20_db")

    cursor = connection.cursor()
    ################################################################
    postgresql_select_query = "select * from pmk_23"

    cursor.execute(postgresql_select_query)
    mobile_records = cursor.fetchmany(2)

    print("Вывод двух строк")
    for row in mobile_records:
        print("Id =", row[0], )
        print("Модель =", row[1])
        print("Цена =", row[2], "\n")

    mobile_records = cursor.fetchmany(2)

    print("Вывод следующих двух строк")
    for row in mobile_records:
        print("Id =", row[0], )
        print("Модель =", row[1])
        print("Цена =", row[2], "\n")

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")