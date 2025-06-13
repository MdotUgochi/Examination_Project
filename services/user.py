from uuid import uuid4, UUID
from fastapi import HTTPException

from schemas.user import UserCreate, UserUpdate
from database import db


def get_all_users():
    return db["users"]

def get_user_by_id(user_id: UUID):
    for user in db["users"]:
        if user["id"] == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

def create_user(user_data: UserCreate):
    new_user = {
        "id": uuid4(),
        "name": user_data.name,
        "email": user_data.email,
        "is_active": True
    }
    db["users"].append(new_user)
    return new_user

def update_user(user_id: UUID, update_data: UserUpdate):
    for user in db["users"]:
        if user["id"] == user_id:
            if update_data.name is not None:
                user["name"] = update_data.name
            if update_data.email is not None:
                user["email"] = update_data.email
            if update_data.is_active is not None:
                user["is_active"] = update_data.is_active
            return user
    raise HTTPException(status_code=404, detail="User not found")

def delete_user(user_id: UUID):
    for i, user in enumerate(db["users"]):
        if user["id"] == user_id:
            return db["users"].pop(i)
    raise HTTPException(status_code=404, detail="User not found")

def deactivate_user(user_id: UUID):
    for user in db["users"]:
        if user["id"] == user_id:
            user["is_active"] = False
            return user
    raise HTTPException(status_code=404, detail="User not found")

