from fastapi import APIRouter, HTTPException
from uuid import UUID
from schemas.registration import RegistrationCreate, RegistrationResponse
from services import registration as registration_service

router = APIRouter()

#create registration
@router.post("/", response_model=RegistrationResponse)
def register_user(data: RegistrationCreate):
    try:
        return registration_service.register_user(data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

#mark attendance
@router.patch("/{registration_id}/attend", response_model=RegistrationResponse)
def mark_attendance(registration_id: UUID):
    try:
        return registration_service.mark_attendance(registration_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

#get list of all registrations
@router.get("/", response_model=list[RegistrationResponse])
def list_registrations():
    return registration_service.get_all_registrations()

#get a specific users registration details
@router.get("/user/{user_id}", response_model=list[RegistrationResponse])
def user_registrations(user_id: UUID):
    return registration_service.get_registrations_by_user(user_id)
