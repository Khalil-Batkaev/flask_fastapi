from typing import List
from fastapi import FastAPI
import databases
from lesson_6.models.new_user import User, CreateUser
from lesson_6.models.goods import Goods, CreateGoods
from lesson_6.models.order import Order, CreateOrder
from lesson_6.db_table_create import create_tables

DATABASE_URL = "sqlite:///mydatabase.db"

database = databases.Database(DATABASE_URL)
app = FastAPI()
users, goods, orders = create_tables()


@app.on_event("startup")
async def db_connect():
    await database.connect()


@app.on_event("shutdown")
async def db_disconnect():
    await database.disconnect()
    
    
# --------------------------USERS---------------------------
@app.post('/users', response_model=User, summary='Create a new user', tags=['Users'])
async def create_user(user: CreateUser):
    query = users.insert().values(**user.dict())
    user_id = await database.execute(query)
    return {**user.dict(), 'id': user_id}


@app.get('/users', response_model=List[User], summary='Read all users', tags=['Users'])
async def read_all_users():
    query = users.select()
    return await database.fetch_all(query)


@app.get('/users/{user_id}', response_model=User, summary='Read the user by id', tags=['Users'])
async def read_user_by_id(user_id: int):
    query = users.select().where(users.c.id == user_id)
    return await database.fetch_one(query)


@app.put('/users/{user_id}', response_model=User, summary='Update the user by id', tags=['Users'])
async def update_user_by_id(user: CreateUser, user_id: int):
    query = users.update().values(**user.dict()).where(users.c.id == user_id)
    await database.execute(query)
    return {**user.dict(), 'id': user_id}


@app.delete('/users/{user_id}', summary='Delete the user by id', tags=['Users'])
async def delete_user_by_id(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    await database.execute(query)
    return {'msg': f'The user with id {user_id} is deleted'}


# --------------------------GOODS---------------------------
@app.post('/goods', response_model=Goods, summary='Create a new goods', tags=['Goods'])
async def create_good(product: CreateGoods):
    query = goods.insert().values(**product.dict())
    goods_id = await database.execute(query)
    return {**product.dict(), 'id': goods_id}


@app.get('/goods', response_model=List[Goods], summary='Read all goods', tags=['Goods'])
async def read_all_goods():
    query = goods.select()
    return await database.fetch_all(query)


@app.get('/goods/{good_id}', response_model=Goods, summary='Read the good by id', tags=['Goods'])
async def read_good_by_id(goods_id: int):
    query = goods.select().where(goods.c.id == goods_id)
    return await database.fetch_one(query)


@app.put('/goods/{good_id}', response_model=Goods, summary='Update the good by id', tags=['Goods'])
async def update_good_by_id(product: CreateGoods, goods_id: int):
    query = goods.update().values(**product.dict()).where(goods.c.id == goods_id)
    await database.execute(query)
    return {**product.dict(), 'id': goods_id}


@app.delete('/goods/{good_id}', summary='Delete the good by id', tags=['Goods'])
async def delete_good_by_id(goods_id: int):
    query = goods.delete().where(goods.c.id == goods_id)
    await database.execute(query)
    return {'msg': f'The good with id {goods_id} is deleted'}
