from pydantic import BaseModel
from uuid import UUID
from datetime import date
from typing import Optional


class RegistrationBase(BaseModel):
    user_id: UUID
    event_id: UUID

class RegistrationCreate(RegistrationBase):
    registration_date: Optional[date] = None

class RegistrationUpdate(BaseModel):
    attended: Optional[bool] = None

class RegistrationResponse(RegistrationBase):
    id: UUID
    registration_date: date
    attended: bool

    class config:
        from_attributes = True