from typing import List

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(
    title="Вебинар"
)

users = [
    {"id": 1, "name": "Вася"},
    {"id": 2, "name": "Коля"},
    {"id": 3, "name": "Леша"},

]


class UserNew(BaseModel):     # валидация(проверка типов) входных данных
    id: int
    name: str = Field(max_length=10)   # max значение символов
    age: int = Field(ge=0)    # больше или равно 0


class User(BaseModel):   # валидация выходных данных
    id: int
    name: str


@app.get("/users/{user_id}", response_model=List[User])   # проверяем отправляемые данные
async def root(user_id: int):
    return [user for user in users if user.get("id") == user_id]


@app.post("/users")
def add_new_user(new_user: List[UserNew]):
    users.extend(new_user)
    return users


@app.post("/users/{user_id}")
def change_name(user_id: int, new_name: str):
    current_user = list(filter(lambda user: user.get("id") == user_id, users))[0]
    current_user["name"] = new_name
    return {"status": 200, "data": current_user}


