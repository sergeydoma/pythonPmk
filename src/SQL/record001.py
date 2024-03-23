import psycopg2
from psycopg2 import Error

try:
	# Подключиться к существующей базе данных
	connection = psycopg2.connect(user = "postgres", # пароль, который указали при установке PostgreSQL
		password = "123", host = "127.0.0.1", port = "5432", database = "pmk20_db")

	cursor = connection.cursor()
	postgreSQL_select_Query = "select * from pmk_23"

	cursor.execute(postgreSQL_select_Query)
	print("Выбор строк из таблицы mobile с помощью cursor.fetchall")
	pmk_records = cursor.fetchall()

	print("Вывод каждой строки и ее столбцов")
	for row in pmk_records:
		if row[3] == '1':
			for row in pmk_records:
				if row[4] == '1':
					print("id =", row[0], )
					print("time =", row[1])
					print("idPMK =", row[2])
					print("numPlat =", row[3])
					print("numCh =", row[4])
					print("Uinput1 =", row[5])
					print("Uinput2 =", row[6])
					print("RZ1 =", row[7])
					print("RZ2 =", row[8])
					print("Rloop =", row[9])
					print("Uvol =", row[10], "\n")

except (Exception, Error) as error:
	print("Ошибка при работе с PostgreSQL", error)
finally:
	if connection:
		cursor.close()
		connection.close()
		print("Соединение с PostgreSQL закрыто")