from fastapi import APIRouter, HTTPException
from typing import List
from uuid import UUID

from schemas.speaker import SpeakerCreate, SpeakerUpdate, SpeakerResponse
from services import speaker as speaker_service
from database import db

router = APIRouter()

@router.get("/", response_model=List[SpeakerResponse])
def get_all_speakers():
    return speaker_service.get_all_speakers()


