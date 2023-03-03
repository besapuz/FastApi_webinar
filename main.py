from fastapi import FastAPI

app = FastAPI(
    title="Вебинар"
)

users = [
    {"id": 1, "name": "Вася"},
    {"id": 2, "name": "Коля"},
    {"id": 3, "name": "Леша"},

]


@app.get("/users/{user_id}")
async def root(user_id: int):
    return [user for user in users if user.get("id") == user_id]


@app.post("/users")
def add_new_user(user_id: int, new_user: str):
    users.append({"id": user_id, "name": new_user})
    return users


@app.post("/users/{user_id}")
def change_name(user_id: int, new_name: str):
    current_user = list(filter(lambda user: user.get("id") == user_id, users))[0]
    current_user["name"] = new_name
    return {"status": 200, "data": current_user}


