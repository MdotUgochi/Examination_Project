from uuid import uuid4, UUID
from database import db

def get_all_speakers(db=db):
    return [
        {
            "speaker_id": s["id"],
            "speaker_full_name": s["name"],
            "topic": s["topic"]
        }
        for s in db["speakers"]
    ]






