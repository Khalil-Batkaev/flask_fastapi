from typing import List, Optional
from random import choice

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Movie(BaseModel):
    id: Optional[int]
    title: str
    description: str
    genre: str


movies = []


@app.get('/add_movie')
async def add_movies():
    for i in range(6):
        movies.append(Movie(id=i, title=f'movie_{i}', description=f'movie_{i}', genre=choice(['drama', 'comedy'])))
    return {'msg': 'ok'}


@app.get('/movie/{genre}', response_model=List[Movie])
async def read_task(genre: str):
    result_movies = []
    for movie in movies:
        if movie.genre == genre:
            result_movies.append(movie)
    if result_movies:
        return result_movies
    raise HTTPException(status_code=404, detail='genre not found')
