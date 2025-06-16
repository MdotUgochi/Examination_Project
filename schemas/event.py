from pydantic import BaseModel
from uuid import UUID
from typing import Optional, List
from datetime import datetime


class Speaker(BaseModel):
    id: UUID
    name: str
    topic: str


class EventBase(BaseModel):
    title: str
    location: str
    date: datetime
    is_open: bool = True


class EventCreate(EventBase):
    speakers: Optional[List[UUID]] = []


class EventUpdate(BaseModel):
    title: Optional[str] = None
    location: Optional[str] = None
    date: Optional[datetime] = None
    is_open: Optional[bool] = None


class Event(BaseModel):
    id: UUID
    title: str
    location: str
    date: datetime
    is_open: bool
    speakers: List[Speaker]