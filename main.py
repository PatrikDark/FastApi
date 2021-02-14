# FastAPI Basics
# from fastapi import FastAPI
# from typing import List, Optional
# from pydantic import BaseModel

# app = FastAPI()



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

# template ....

# from fastapi import FastAPI, Request, Form
# from fastapi.templating import Jinja2Templates


# app = FastAPI()
# templates = Jinja2Templates(directory="templates/")

# @app.get('/')
# def read_form():
#     return 'hello world'


# @app.get("/form")
# def form_post(request: Request):
#     result = "Type a number"
#     return templates.TemplateResponse('index.html', context={'request': request, 'result': result})


# @app.post("/form")
# def form_post(request: Request, num: int = Form(...)):
#     result = num
#     return templates.TemplateResponse('index.html', context={'request': request, 'result': result})

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

class Todo(BaseModel):
    name: str
    time: str
    description: str

app = FastAPI(title="Todo API")

tasks = []

@app.get('/')
async def home():
    return "Hello welcome to the Todo api"

@app.get('/todo/')
async def all_todo():
    return tasks

@app.post('/todo/')
async def add_todo(todo: Todo):
    tasks.append(todo)
    return todo

@app.get('/todo/{id}')
async def get_todo(id: int):
    try:
        return tasks[id]
    except:
        raise HTTPException(status_code=404, detail='id is invalid')

@app.put('/todo/{id}')
async def get_todo(id: int, updated_todo: Todo):
    try:
        tasks[id] = updated_todo
        return updated_todo
    except:
        raise HTTPException(status_code=404, detail='id is invalid')

@app.delete('/todo/{id}')
async def get_todo(id: int):
    try:
        todo = tasks[id]
        tasks.pop(id)
        return todo
    except:
        raise HTTPException(status_code=404, detail='id is invalid')



