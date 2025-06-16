from fastapi import APIRouter
from uuid import uuid4, UUID
from typing import List

from schemas.user import User, UserCreate, UserUpdate
from services import user as user_service
from services.user import get_users_who_attended_atleast_one_event

router = APIRouter()

@router.get("/", response_model=List[User])
def list_users():
    return user_service.get_all_users()

@router.get("/{user_id}", response_model=User)
def get_user(user_id: UUID):
    return user_service.get_user_by_id(user_id)

@router.post("/", response_model=User, status_code=201)
def create_user(user_data: UserCreate):
    return user_service.create_user(user_data)

@router.put("/{user_id}", response_model=User)
def update_user(user_id: UUID, update_data: UserUpdate):
    return user_service.update_user(user_id, update_data)

@router.delete("/{user_id}", response_model=User)
def delete_user(user_id: UUID):
    return user_service.delete_user(user_id)

@router.patch("/{user_id}/deactivate", response_model=User)
def deactivate_user(user_id: UUID):
    return user_service.deactivate_user(user_id)

@router.get("/users/filter_attended", response_model=List[User])
def users_who_attended():
    return get_users_who_attended_atleast_one_event()