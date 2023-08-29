from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel

from app.api.schemas.selected_options_schemas import SelectedOptions


class ReportBase(BaseModel):
    qualitative: str
    quantitative: str
    selected_report: str  # Updated type
    comment: str
    agree: bool


class ReportCreate(ReportBase):
    pass


class Report(ReportBase):
    id: int
    created_at: datetime
    user_id: int
    selectedoptions: List[SelectedOptions] = []  # Corrected field name

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True
