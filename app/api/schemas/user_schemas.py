from typing import List
from datetime import datetime
from pydantic import BaseModel

from app.api.schemas.report_schemas import Report


class UserBase(BaseModel):
    token: str


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int
    created_at: datetime
    reports: list[Report] = []

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True
