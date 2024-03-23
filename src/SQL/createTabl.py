
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

    # Создайте курсор для выполнения операций с базой данных
    cursor = connection.cursor()
    # SQL-запрос для создания новой таблицы
    create_table_query = '''CREATE TABLE pmk
                          ( 
                            c_id SERIAL PRIMARY KEY,
                            TIME            TIMESTAMPTZ,
                            IDPMK           BYTEA,
                            NumPlat         INT,
                            NumCh           INT,
                            Uinput1         FLOAT,
                            Uinput2         FLOAT,
                            RZ1             FLOAT,
                            RZ2             FLOAT,
                            RLOOP           FLOAT,
                            Uvol            FLOAT
                            ); '''
    # Выполнение команды: это создает новую таблицу
    cursor.execute(create_table_query)
    connection.commit()
    print("Таблица успешно создана в PostgreSQL")

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")