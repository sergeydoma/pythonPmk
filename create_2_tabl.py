
import psycopg2
from psycopg2 import Error

try:
    # Подключиться к существующей базе данных
    connection = psycopg2.connect(user="postgres",
                                  # пароль, который указали при установке PostgreSQL
                                  password="123",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="postgres_db")

    # Создайте курсор для выполнения операций с базой данных
    cursor = connection.cursor()
    # SQL-запрос для создания новой таблицы
    create_table_rz1 = '''CREATE TABLE IF NOT EXISTS RZ1
                          (Id SERIAL        PRIMARY KEY,
                            TIME            TIMESTAMPTZ,
                            CHANAL_1           INT,
                            CHANAL_2           INT,
                            CHANAL_3           INT,
                            CHANAL_4           INT,
                            CHANAL_5           INT,
                            CHANAL_6           INT,
                            CHANAL_7           INT,
                            CHANAL_8           INT,
                            CHANAL_9           INT,
                            CHANAL_10           INT
                                ); 
                            '''
    # Выполнение команды: это создает новую таблицу
    cursor.execute(create_table_rz1)
    connection.commit()
    print("Таблица успешно создана в PostgreSQL")

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")