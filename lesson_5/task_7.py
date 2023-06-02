from typing import List, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

"""
Создать RESTful API для управления списком задач. Приложение должно
использовать FastAPI и поддерживать следующие функции:
○ Получение списка всех задач.
○ Получение информации о задаче по её ID.
○ Добавление новой задачи.
○ Обновление информации о задаче по её ID.
○ Удаление задачи по её ID.
Каждая задача должна содержать следующие поля: ID (целое число),
Название (строка), Описание (строка), Статус (строка): "todo", "in progress",
"done".
Создайте модуль приложения и настройте сервер и маршрутизацию.
Создайте класс Task с полями id, title, description и status.
Создайте список tasks для хранения задач.
Создайте функцию get_tasks для получения списка всех задач (метод GET).
Создайте функцию get_task для получения информации о задаче по её ID
(метод GET).
Создайте функцию create_task для добавления новой задачи (метод POST).
Создайте функцию update_task для обновления информации о задаче по её ID
(метод PUT).
Создайте функцию delete_task для удаления задачи по её ID (метод DELETE).
"""

app = FastAPI()
STATUS = ("todo", "in progress", "done")

tasks = []


class Task(BaseModel):
    id: Optional[int]
    title: str
    description: str
    status: str = STATUS[0]
    is_deleted: bool = False


@app.get('/tasks', response_model=List[Task])
async def read_tasks():
    return tasks


@app.get('/tasks/{task_id}', response_model=Task)
async def read_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail='task not found')


@app.post('/tasks', response_model=Task)
async def create_task(task: Task):
    if task.status not in STATUS:
        raise HTTPException(status_code=400, detail='wrong status')

    task.id = tasks[-1].id + 1 if tasks else 1
    tasks.append(task)
    return task


@app.put('/tasks/{task_id}', response_model=Task)
async def update_task(task_id: int, task: Task):
    if task.status not in STATUS:
        raise HTTPException(status_code=400, detail='wrong status')

    for i, _task in enumerate(tasks):
        if task_id == _task.id:
            task.id = task_id
            tasks[i] = task
            return task
    raise HTTPException(status_code=404, detail='task not found')


@app.delete('/tasks/{task_id}')
async def update_task(task_id: int):
    for i, _task in enumerate(tasks):
        if task_id == _task.id:
            tasks[i].is_deleted = True
            return {'msg': f'task {task_id} is deleted'}
    raise HTTPException(status_code=404, detail='task not found')
