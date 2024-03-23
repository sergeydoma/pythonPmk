

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base

engine = create_engine('postgresql://postgres:123@localhost/pmk20_db')
engine.connect()  # подключение к бд
# функция, которая создает базовый класс для декларативных классов
Base = declarative_base()


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key = True)
    name = Column(String)


Base.metadata.create_all(engine)  # создание всех таблиц