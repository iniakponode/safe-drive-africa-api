from array import array

from pydantic import BaseModel


class SelectedOptionsBase(BaseModel):
    select_opt: str  # Corrected field name


class SelectedOptionsCreate(SelectedOptionsBase):
    pass


class SelectedOptions(SelectedOptionsBase):
    id: int
    reports_id: int

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True
