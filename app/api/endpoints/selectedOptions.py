from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.api.database.base import Base, engine
from app.api.database.queries.report_queries import get_report_by_id
from app.api.database.queries.selectedoptions_queries import create_selected_options, get_selected_options_by_report
from app.api.database.dependency.db_instance import get_db
from app.api.schemas.selected_options_schemas import SelectedOptionsCreate, SelectedOptions

Base.metadata.create_all(bind=engine)

router = APIRouter()


@router.post("/selected-options/", response_model=SelectedOptions)
def create_report_selected_options(selected_options: SelectedOptionsCreate, reports_id: int, db: Session = Depends(get_db)):
    report = get_report_by_id(db, reports_id)
    if report is None:
        raise HTTPException(status_code=404, detail="report with that id is not found")
    return create_selected_options(db, reports_id, selected_options.select_opt)


@router.get("/reports/{report_id}/selected-options/", response_model=List[SelectedOptions])
def get_report_selected_options(report_id: int, db: Session = Depends(get_db)):
    selected_options = get_selected_options_by_report(db, report_id)
    if not selected_options:
        raise HTTPException(status_code=404, detail="Selected options not found for report")
    return selected_options
