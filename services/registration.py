from uuid import uuid4, UUID
from datetime import date, datetime
from typing import List

from database import db
from schemas.registration import RegistrationCreate, RegistrationResponse


def register_user(data: RegistrationCreate) -> RegistrationResponse:
    #check if user exists and is active
    user = next((u for u in db["users"] if u["id"] == data.user_id and u["is_active"]), None)
    if not user:
        raise ValueError("User not found or not active")
    
    #check if event exists and is open
    event = next((e for e in db["events"] if e["id"] == data.event_id), None)
    if not event:
        raise ValueError("Event not found")
    if not event.get("is_open", False):
        raise ValueError("Event is not open for registration")
    
    #check if user already registered for the event
    already_registered = next(
        (r for r in db["registrations"] if r["user_id"] == data.user_id and r["event_id"] == data.event_id),
        None
    )
    if already_registered:
        raise ValueError("User already registered for this event")
    
    #Register User
    registration = {
        "id": uuid4(),
        "user_id": data.user_id,
        "event_id": data.event_id,
        "registration_date": data.registration_date or data.today(),
        "attended": False
    }
    db["registrations"].append(registration)
    return RegistrationResponse(**registration)

def mark_attendance(registration_id: UUID) -> RegistrationResponse:
    registration = next((r for r in db["registrations"] if str(r["id"]) == str(registration_id)), None)
    if not registration:
        raise ValueError("Registration not found")
    
    registration["attended"] = True
    return RegistrationResponse(**registration)

def get_registrations_by_user(user_id: UUID) -> List[RegistrationResponse]:
    return [
        RegistrationResponse(**r)
        for r in db["registrations"]
        if r["user_id"] == user_id
    ]

def get_all_registrations() -> List[RegistrationResponse]:
    return [RegistrationResponse(**r) for r in db["registrations"]]
