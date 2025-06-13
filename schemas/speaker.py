from pydantic import BaseModel
from uuid import UUID
from typing import Optional


class SpeakerBase(BaseModel):
    speaker_id: UUID
    speaker_full_name: str
    topic: str


class SpeakerCreate(SpeakerBase):
    speaker_full_name: str
    topic: str

class SpeakerUpdate(SpeakerCreate):
    speaker_full_name: Optional[str] = None
    topic: Optional[str] = None


class SpeakerResponse(SpeakerBase):
    speaker_id: UUID
    speaker_full_name: str
    topic: str