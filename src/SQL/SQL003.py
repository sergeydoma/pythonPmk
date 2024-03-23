from datetime import datetime

from sqlalchemy import (create_engine, Column, Integer, String, select, update, DateTime, TIMESTAMP, func)
from sqlalchemy.orm import declarative_base, Session, mapped_column





engine = create_engine('postgresql://postgres:123@localhost/pmk20_db')
engine.connect()
Base = declarative_base()
session = Session(engine)


class User(Base):
	__tablename__ = "user"
	id = Column(Integer, primary_key = True)
	name = Column(String)
	last_time = Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp())




# SELECT
def selectUser():
	result = session.execute(select(User))  # поиск всех данных с таблицы
	for data in result.scalars():
		print(f"id: {data.id} | name: {data.name}")


# INSERT
def addUser(id: int, name: str):
	session.add(User(id = id, name = name))  # добавление новых данных
	date_added=datetime.today()
	session.commit()


# DELETE by id
def deleteUser(id: int):
	session.query(User).filter(User.id == id).delete()  # поиск и удаление ряда
	session.commit()


# UPDATE name by id
def updateUser(id: int, new_name: str):
	session.execute(update(User).where(User.id == id).values(name = new_name))  # поиск и обновление значений
	session.commit()


if 1 == 1:
	Base.metadata.drop_all(engine)  # удаление таблиц
	# Base.metadata.create_all(engine)  # создание таблиц
	# addUser(id = 3, name = "name")
	# addUser(id = 4, name = 'Sergey')
	# selectUser()
	# updateUser(id = 4, new_name = "new_name")
	# selectUser()
	# deleteUser(1)
	# selectUser()