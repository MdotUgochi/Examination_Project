from typing import List, Optional
from uuid import UUID, uuid4
from datetime import datetime
import copy
from database import db
from schemas.event import EventBase, EventCreate, EventUpdate, Event


def create_event (event_data: EventCreate):
     new_event = {
         "id": uuid4(),
         "title": event_data.title,
         "location": event_data.location,
         "date": event_data.date,
         "is_open": True,
         "speakers": db["speakers"] #automatically assign all users
     }

     db["events"].append(new_event)
     return new_event
   

def get_event(event_id: UUID) -> Optional[Event]:
    for event in db["events"]:
        if event["id"] == event_id:
            return _dict_to_event_model(event)
    return None
    

def get_all_events() -> List[Event]:
    results = []
    print("Fecth all events")
    for events in db["events"]:
        try:
            model = _dict_to_event_model(events)
            results.append(model)
        except Exception as e:
             print("Error converting event:", events)
             print("Exception:", e)
    return results
    


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
    
    # Safely try to convert speakers into Speaker model list
    speakers_raw = data.get("speakers", [])
    valid_speakers = []

    for s in speakers_raw:
        try:
            
            # If speaker fields are valid
            valid_speakers.append({
                "id": UUID(s["id"]) if isinstance(s["id"], str) else s["id"],
                "name": s["name"],
                "topic": s["topic"]
            })
        except Exception as e:
            print(f"⚠️ Skipping invalid speaker: {s} -> {e}")

    return Event(
        id=data["id"],
        title=data["title"],
        location=data["location"],
        date=data["date"],
        is_open=data.get("is_open", True),
        speakers=valid_speakers
        )


