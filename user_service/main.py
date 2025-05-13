
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import uuid

app = FastAPI()

# Simulación de base de datos
db = {}

class User(BaseModel):
    id: Optional[str]
    name: str
    email: str
    role: str  # 'patient' or 'doctor'

@app.post("/register")
def register(user: User):
    user.id = str(uuid.uuid4())
    db[user.id] = user
    return {"message": "User registered", "user_id": user.id}

@app.get("/user/{user_id}")
def get_user(user_id: str):
    if user_id not in db:
        raise HTTPException(status_code=404, detail="User not found")
    return db[user_id]

@app.put("/user/{user_id}")
def update_user(user_id: str, updated_user: User):
    if user_id not in db:
        raise HTTPException(status_code=404, detail="User not found")
    updated_user.id = user_id
    db[user_id] = updated_user
    return {"message": "User updated", "user": updated_user}
