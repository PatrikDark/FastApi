# FastAPI Basics
from fastapi import FastAPI
from typing import List, Optional
from pydantic import BaseModel

app = FastAPI()



# @app.get('/')
# async def root():
#     return "Welcome to the home page"

# @app.get('/show_message/{your_message}')
# async def message(message: int):
#     return message
 
# @app.get('/info/')
# async def info(name: str, age: int):
#     if age < 18:
#         return f'Hello {name} you are tenager'
#     return f'Name: {name} Age: {age}'

# class User(BaseModel):
#     id: int
#     name: str
#     friends: List[str] = []
#     gender : Optional[str] = ''


# @app.post('/user/')
# async def add_user(user: User):
#     return user


# @app.post('/user_status/')
# async def add_user(status: str, user: User):
#     return {"Status": status, **user.dict()}



