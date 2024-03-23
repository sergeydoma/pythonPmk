from sqlalchemy import create_engine

# <dialect+driver>://<user>@<ip:port>/<database>
engine = create_engine('postgresql://postgres:pass@localhost/postgres')
engine.connect()
print(engine)
#Создания таблиц
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base

engine = create_engine('postgresql://postgres:@localhost/postgres')
engine.connect()  # подключение к бд
# функция, которая создает базовый класс для декларативных классов
Base = declarative_base()


class User(Base):
	__tablename__ = "user"
	id = Column(Integer, primary_key = True)
	name = Column(String)


Base.metadata.create_all(engine)  # создание всех таблиц

from sqlalchemy import (create_engine, Column, Integer, String, select, update)
from sqlalchemy.orm import declarative_base, Session

engine = create_engine('postgresql://postgres:pass@localhost/postgres')
engine.connect()
Base = declarative_base()
session = Session(engine)


class User(Base):
	__tablename__ = "user"
	id = Column(Integer, primary_key = True)
	name = Column(String)
	timestamp =


# SELECT
def selectUser():
	result = session.execute(select(User))  # поиск всех данных с таблицы
	for data in result.scalars():
		print(f"id: {data.id} | name: {data.name}")


# INSERT
def addUser(id: int, name: str):
	session.add(User(id = id, name = name))  # добавление новых данных
	session.commit()


# DELETE by id
def deleteUser(id: int):
	session.query(User).filter(User.id == id).delete()  # поиск и удаление ряда
	session.commit()


# UPDATE name by id
def updateUser(id: int, new_name: str):
	session.execute(update(User).where(User.id == id).values(name = new_name))  # поиск и обновление значений
	session.commit()


if __name__ == '__main__':
	# Base.metadata.drop_all(engine)  # удаление таблиц
	Base.metadata.create_all(engine)  # создание таблиц
	addUser(id = 1, name = "name")
	selectUser()
	updateUser(id = 1, new_name = "new_name")
	selectUser()
	deleteUser(1)
	selectUser()