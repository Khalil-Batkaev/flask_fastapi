from typing import List, Optional

from fastapi import FastAPI, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI()
templates = Jinja2Templates(directory="lesson_5/templates")


class User(BaseModel):
    id: Optional[int]
    name: str
    email: str
    password: str
    is_deleted: bool = False


users = []


@app.on_event("startup")
async def add_users():
    for i in range(6):
        users.append(User(id=i, name=f'user_{i}', email=f'user_{i}@test.ru', password=f'hash_password_{i}'))
    return {'msg': 'ok'}


@app.get('/users/html', response_class=HTMLResponse)
async def read_users_html(request: Request):
    return templates.TemplateResponse('users.html', context={'request': request, 'users': users})


@app.get('/users', response_model=List[User])
async def read_users():
    return users


@app.post('/users', response_model=User)
async def create_user(user: User):
    user_id = users[-1].id if users else 0
    user.id = user_id + 1
    users.append(user)
    return user


@app.put('/users/{user_id}', response_model=User)
async def update_user(user_id: int, user: User):
    for i, _user in enumerate(users):
        if _user.id == user_id:
            users[i] = user
            return user
    raise HTTPException(status_code=404, detail='user not found')


@app.delete('/users/{user_id}')
async def delete_user(user_id: int):
    for i, _user in enumerate(users):
        if _user.id == user_id:
            users[i].is_deleted = True
            return {'msg': f'user {user_id} is deleted'}
    raise HTTPException(status_code=404, detail='user not found')
