from typing import List
from fastapi import FastAPI
import databases
from lesson_6.models.user import User, CreateUser
from lesson_6.models.task import Task, CreateTask
from lesson_6.db_table_create import create_table

DATABASE_URL = "sqlite:///mydatabase.db"

database = databases.Database(DATABASE_URL)
app = FastAPI()
users, tasks = create_table()


@app.on_event("startup")
async def db_connect():
    await database.connect()


@app.on_event("shutdown")
async def db_disconnect():
    await database.disconnect()


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


@app.get('/tasks', response_model=List[Task], summary='Read all tasks', tags=['Tasks'])
async def read_all_tasks():
    query = tasks.select()
    return await database.fetch_all(query)


@app.get('/tasks/{task_id}', response_model=Task, summary='Read the task by id', tags=['Tasks'])
async def read_task_by_id(task_id: int):
    query = tasks.select().where(tasks.c.id == task_id)
    return await database.fetch_one(query)


@app.post('/tasks', response_model=Task, summary='Create a new task', tags=['Tasks'])
async def create_task(task: CreateTask):
    query = tasks.insert().values(**task.dict())
    task_id = await database.execute(query)
    return {**task.dict(), 'id': task_id}


@app.put('/tasks/{task_id}', response_model=Task, summary='Update the task by id', tags=['Tasks'])
async def update_task_by_id(task: CreateTask, task_id: int):
    query = tasks.update().values(**task.dict()).where(tasks.c.id == task_id)
    await database.execute(query)
    return {**task.dict(), 'id': task_id}


@app.delete('/task/{task_id}', summary='Delete the task by id', tags=['Tasks'])
async def delete_task(task_id: int):
    query = tasks.delete().where(tasks.c.id == task_id)
    await database.execute(query)
    return {'msg': f'The task with id {task_id} is deleted'}
