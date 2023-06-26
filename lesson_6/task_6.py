from typing import List
from fastapi import FastAPI, HTTPException
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
    if user_id:
        return {**user.dict(), 'id': user_id}
    raise HTTPException(status_code=500, detail='DB connect error')


@app.get('/users', response_model=List[User], summary='Read all users', tags=['Users'])
async def read_all_users():
    query = users.select()
    return await database.fetch_all(query)


@app.get('/users/{user_id}', response_model=User, summary='Read the user by id', tags=['Users'])
async def read_user_by_id(user_id: int):
    query = users.select().where(users.c.id == user_id)
    _user = await database.fetch_one(query)
    if _user:
        return _user
    raise HTTPException(status_code=404, detail='user not found')


@app.put('/users/{user_id}', response_model=User, summary='Update the user by id', tags=['Users'])
async def update_user_by_id(user: CreateUser, user_id: int):
    query = users.update().values(**user.dict()).where(users.c.id == user_id)
    _user = await database.execute(query)
    if _user:
        return {**user.dict(), 'id': user_id}
    raise HTTPException(status_code=404, detail='user not found')


@app.delete('/users/{user_id}', summary='Delete the user by id', tags=['Users'])
async def delete_user_by_id(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    _user = await database.execute(query)
    if _user:
        return {'msg': f'The user with id {user_id} is deleted'}
    raise HTTPException(status_code=404, detail='user not found')


# --------------------------GOODS---------------------------
@app.post('/goods', response_model=Goods, summary='Create a new goods', tags=['Goods'])
async def create_product(product: CreateGoods):
    query = goods.insert().values(**product.dict())
    goods_id = await database.execute(query)
    if goods_id:
        return {**product.dict(), 'id': goods_id}
    raise HTTPException(status_code=500, detail='DB connect error')


@app.get('/goods', response_model=List[Goods], summary='Read all goods', tags=['Goods'])
async def read_all_goods():
    query = goods.select()
    return await database.fetch_all(query)


@app.get('/goods/{goods_id}', response_model=Goods, summary='Read the good by id', tags=['Goods'])
async def read_product_by_id(goods_id: int):
    query = goods.select().where(goods.c.id == goods_id)
    _goods = await database.fetch_one(query)
    if _goods:
        return _goods
    raise HTTPException(status_code=404, detail='product not found')


@app.put('/goods/{goods_id}', response_model=Goods, summary='Update the good by id', tags=['Goods'])
async def update_product_by_id(product: CreateGoods, goods_id: int):
    query = goods.update().values(**product.dict()).where(goods.c.id == goods_id)
    _goods = await database.execute(query)
    if _goods:
        return {**product.dict(), 'id': goods_id}
    raise HTTPException(status_code=404, detail='product not found')


@app.delete('/goods/{goods_id}', summary='Delete the good by id', tags=['Goods'])
async def delete_product_by_id(goods_id: int):
    query = goods.delete().where(goods.c.id == goods_id)
    _goods = await database.execute(query)
    if _goods:
        return {'msg': f'The good with id {goods_id} is deleted'}
    raise HTTPException(status_code=404, detail='product not found')


# --------------------------ORDERS---------------------------
@app.post('/orders', response_model=Order, summary='Create a new order', tags=['Orders'])
async def create_order(order: CreateOrder):
    query = orders.insert().values(**order.dict())
    orders_id = await database.execute(query)
    if orders_id:
        return {**order.dict(), 'id': orders_id}
    raise HTTPException(status_code=500, detail='DB connect error')


@app.get('/orders', response_model=List[Order], summary='Read all orders', tags=['Orders'])
async def read_all_orders():
    query = orders.select()
    return await database.fetch_all(query)


@app.get('/orders/{order_id}', response_model=Order, summary='Read the order by id', tags=['Orders'])
async def read_order_by_id(order_id: int):
    query = orders.select().where(orders.c.id == order_id)
    _order = await database.fetch_one(query)
    if _order:
        return _order
    raise HTTPException(status_code=404, detail='order not found')


@app.put('/orders/{order_id}', response_model=Order, summary='Update the order by id', tags=['Orders'])
async def update_order_by_id(order: CreateOrder, order_id: int):
    query = orders.update().values(**order.dict()).where(orders.c.id == order_id)
    _order = await database.execute(query)
    if _order:
        return {**order.dict(), 'id': order_id}
    raise HTTPException(status_code=404, detail='order not found')


@app.delete('/orders/{order_id}', summary='Delete the order by id', tags=['Orders'])
async def delete_order_by_id(order_id: int):
    query = orders.delete().where(orders.c.id == order_id)
    _order = await database.execute(query)
    if _order:
        return {'msg': f'The order with id {order_id} is deleted'}
    raise HTTPException(status_code=404, detail='order not found')
