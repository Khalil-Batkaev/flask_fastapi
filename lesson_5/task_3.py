from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

"""
Создать веб-страницу для отображения списка пользователей. Приложение должно использовать шаблонизатор Jinja для 
динамического формирования HTML страницы.
Создайте модуль приложения и настройте сервер и маршрутизацию.
Создайте класс User с полями id, name, email и password.
Создайте список users для хранения пользователей.
Создайте HTML шаблон для отображения списка пользователей. Шаблон должен содержать заголовок страницы, таблицу со 
списком пользователей и кнопку для добавления нового пользователя.
Создайте маршрут для отображения списка пользователей (метод GET).
Реализуйте вывод списка пользователей через шаблонизатор Jinja
"""


app = FastAPI()
templates = Jinja2Templates(directory="lesson_5/templates")


class User(BaseModel):
    id: int
    name: str
    email: str
    password: str


users = []


@app.on_event("startup")
async def add_users():
    for i in range(6):
        users.append(User(id=i, name=f'movie_{i}', email=f'movie_{i}@test.ru', password=f'movie_{i}'))
    return {'msg': 'ok'}


@app.get('/users', response_class=HTMLResponse)
async def read_users(request: Request):
    return templates.TemplateResponse('index.html', context={'request': request, 'users': users})
