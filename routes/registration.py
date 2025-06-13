from fastapi import APIRouter
from uuid import uuid4, UUID

from schemas.registration import RegistrationCreate, RegistrationResponse
from services import registration as registration_service


router = APIRouter()

@router.post("/", response_model=RegistrationResponse)
def register_user(data: RegistrationCreate):
    return registration_service.register_user(data)


@router.patch("/{registration_id}/attend", response_model=RegistrationResponse)
def mark_attendance(registration_id: UUID):
    return registration_service.mark_attendance(registration_id)


@router.get("/", response_model=list[RegistrationResponse])
def list_registrations():
    return registration_service.get_all_registrations()


@router.get("/user/{user_id}", response_model=list[RegistrationResponse])
def user_registrations(user_id: UUID):
    return registration_service.get_registrations_by_user(user_id)
