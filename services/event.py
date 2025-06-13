from typing import List, Optional
from uuid import UUID, uuid4
from datetime import datetime
from database import db

from schemas.event import EventBase, EventCreate, EventUpdate, Event

#In-memory db for events

def create_event(event_data: EventCreate) -> Event:
    event_id = uuid4()
    new_event = {
        "id": event_id,
        "title": event_data.title,
        "location": event_data.location,
        "date": event_data.date,
        "is_open": True
    }

    db["events"].append(new_event)
    return new_event




def get_event(event_id: UUID) -> Optional[Event]:
    for event in db["events"]:
        if event["id"] == event_id:
            return _dict_to_event_model(event)
    return None
    

def get_all_events() -> List[Event]:
    return [_dict_to_event_model(event) for event in db["events"]]


def update_event(event_id: UUID, update_data: EventUpdate) -> Optional[Event]:
    for event in db["events"]:
        if event["id"] == event_id:
            if update_data.title is not None:
                event["title"] = update_data.title
            if update_data.location is not None:
                event["location"] = update_data.location
            if update_data.date is not None:
                    event["date"] = update_data.date
            if update_data.is_open  is not None:
                event["is_open"] = update_data.is_open
            return _dict_to_event_model(event)
    return None


def close_event_registration(event_id: UUID) -> Optional[Event]:
    for event in db["events"]:
        if event["id"] == event_id:
            event["is_open"] = False
            return _dict_to_event_model(event)
    return None

def delete_event(event_id: UUID) -> bool:
    for i, event in enumerate(db["events"]):
        if event["id"] == event_id:
            del db["events"][i]
        return True
    return False


def _dict_to_event_model(data: dict) -> Event:
    return Event(
        id=data["id"],
        title=data["title"],
        location=data["location"],
        date=data["date"],
        is_open=data["is_open"]
    )
 

