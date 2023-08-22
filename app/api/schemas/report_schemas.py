from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class ReportBase(BaseModel):
    qualitative: str
    quantitative: str
    selected_report: str
    comment: str
    agree: bool


class ReportCreate(ReportBase):
    pass


class Report(ReportBase):
    id: int
    created_at: datetime
    user_id: int

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True
