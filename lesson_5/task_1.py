from typing import List, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

"""
Создать API для управления списком задач. Приложение должно иметь возможность создавать, обновлять, удалять и 
получать список задач.
Создайте модуль приложения и настройте сервер и маршрутизацию.
Создайте класс Task с полями id, title, description и status.
Создайте список tasks для хранения задач.
Создайте маршрут для получения списка задач (метод GET).
Создайте маршрут для создания новой задачи (метод POST).
Создайте маршрут для обновления задачи (метод PUT).
Создайте маршрут для удаления задачи (метод DELETE).
Реализуйте валидацию данных запроса и ответа.
"""

app = FastAPI()


class Task(BaseModel):
    id: Optional[int]
    title: str
    description: str
    status: bool = True


tasks = []


@app.get('/tasks', response_model=List[Task])
async def read_tasks():
    return tasks


@app.get('/tasks/{task_id}', response_model=Task)
async def read_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task
    return HTTPException(status_code=404, detail='task not found')


@app.post('/tasks', response_model=Task)
async def create_task(task: Task):
    old_id = tasks[-1].id if tasks else 0
    task.id = old_id + 1
    tasks.append(task)
    return task


@app.put('/tasks/{task_id}', response_model=Task)
async def update_task(task_id: int, task: Task):
    for i, _task in enumerate(tasks):
        if task_id == _task.id:
            tasks[i] = task
            return task
    return HTTPException(status_code=404, detail='task not found')


@app.delete('/tasks/{task_id}')
async def update_task(task_id: int):
    for i, _task in enumerate(tasks):
        if task_id == _task.id:
            tasks[i].status = False
            return {'msg': 'all done'}
    return HTTPException(status_code=404, detail='task not found')
