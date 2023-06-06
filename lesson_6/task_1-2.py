from typing import List
from fastapi import FastAPI
import databases
import sqlalchemy

from lesson_6.models.user import User, CreateUser

"""
Создать веб-приложение на FastAPI, которое будет предоставлять API для
работы с базой данных пользователей. Пользователь должен иметь
следующие поля:
○ ID (автоматически генерируется при создании пользователя)
○ username:
○ password:
○ Имя (строка, не менее 2 символов)
○ Фамилия (строка, не менее 2 символов)
○ Дата рождения (строка в формате "YYYY-MM-DD")
○ Email (строка, валидный email)
○ Адрес (строка, не менее 5 символов)
API должен поддерживать следующие операции:
○ Добавление пользователя в базу данных
○ Получение списка всех пользователей в базе данных
○ Получение пользователя по ID
○ Обновление пользователя по ID
○ Удаление пользователя по ID
Приложение должно использовать базу данных SQLite3 для хранения
пользователей.
"""

DATABASE_URL = "sqlite:///mydatabase.db"

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()
users = sqlalchemy.Table('users',
                         metadata,
                         sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
                         sqlalchemy.Column("username", sqlalchemy.String(32)),
                         sqlalchemy.Column("password", sqlalchemy.String(32)),
                         sqlalchemy.Column("first_name", sqlalchemy.String(128)),
                         sqlalchemy.Column("last_name", sqlalchemy.String(128)),
                         sqlalchemy.Column("birth_date", sqlalchemy.Date),
                         sqlalchemy.Column("email", sqlalchemy.String(128)),
                         sqlalchemy.Column("address", sqlalchemy.String(128)),
                         )
engine = sqlalchemy.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
metadata.create_all(engine)

app = FastAPI()


@app.on_event("startup")
async def db_connect():
    await database.connect()


@app.on_event("shutdown")
async def db_disconnect():
    await database.disconnect()


@app.post('/users', response_model=User, summary='Create a new user')
async def create_user(user: CreateUser):
    query = users.insert().values(**user.dict())
    user_id = await database.execute(query)
    return {**user.dict(), 'id': user_id}


@app.get('/users', response_model=List[User], summary='Read all users')
async def read_all_users():
    query = users.select()
    return await database.fetch_all(query)


@app.get('/users/{user_id}', response_model=User, summary='Read the user by id')
async def read_user_by_id(user_id: int):
    query = users.select().where(users.c.id == user_id)
    return await database.fetch_one(query)


@app.put('/users/{user_id}', response_model=User, summary='Update the user by id')
async def update_user_by_id(user: CreateUser, user_id: int):
    query = users.update().values(**user.dict()).where(users.c.id == user_id)
    await database.execute(query)
    return {**user.dict(), 'id': user_id}


@app.delete('/users/{user_id}', summary='Delete the user by id')
async def delete_user_by_id(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    await database.execute(query)
    return {'msg': f'The user with id {user_id} is deleted'}
