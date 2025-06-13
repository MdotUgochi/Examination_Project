from pydantic import BaseModel
from uuid import UUID
from typing import Optional
from datetime import datetime

class EventBase(BaseModel):
    title: str
    location: str
    date: datetime
    is_open: bool = True


class EventCreate(EventBase):
    pass


class EventUpdate(BaseModel):
    title: Optional[str] = None
    location: Optional[str] = None
    date: Optional[datetime] = None
    is_open: Optional[bool] = None


class Event(EventBase):
    id: UUID