from fastapi import APIRouter, HTTPException, status
from uuid import UUID
from typing import List

from schemas.event import EventCreate, EventUpdate, Event
from services import event as event_service

router = APIRouter()


@router.post("/", response_model=Event, status_code=status.HTTP_201_CREATED)
def create_event(event_data: EventCreate):
    return event_service.create_event(event_data)


@router.get("/", response_model=List[Event])
def get_all_events():
    return event_service.get_all_events()


@router.get("/{event_id}", response_model=Event)
def get_event_by_id(event_id: UUID):
    event = event_service.get_event(event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event


@router.delete("/{event_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_event(event_id: UUID):
    success = event_service.delete_event(event_id)
    if not success:
        raise HTTPException(status_code=404, detail="Event not found")


@router.patch("/{event_id}/close", response_model=Event)
def close_event(event_id: UUID):
    closed_event = event_service.close_event_registration(event_id)
    if not closed_event:
        raise HTTPException(status_code=404, details="Event not found")
    return closed_event