from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.database.queries.report_queries import create_report, get_report_by_id, delete_report, get_all_reports
from app.api.database.queries.user_queries import get_user_by_id
from app.api.schemas.report_schemas import ReportCreate, Report
from app.api.database.dependency.db_instance import get_db
from app.api.database.base import Base, engine

Base.metadata.create_all(bind=engine)

router = APIRouter()


@router.get("/reports/", response_model=list[Report])
async def get_all_reports(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    report = get_all_reports(db, skip=skip, limit=limit)
    if report is None:
        raise HTTPException(status_code=404, detail="No Reports found")
    return report


@router.post("/reports/", response_model=Report)
async def create_new_report(report_data: ReportCreate, user_id: int, db: Session = Depends(get_db)):
    user = get_user_by_id(db, user_id)

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    report = create_report(db, user_id, **report_data.model_dump())
    return report


@router.get("/reports/{report_id}/", response_model=Report)
async def get_report(report_id: int, db: Session = Depends(get_db)):
    report = get_report_by_id(db, report_id)
    if report is None:
        raise HTTPException(status_code=404, detail="Report not found")
    return report


@router.delete("/reports/{report_id}/")
async def delete_report_by_id(report_id: int, db: Session = Depends(get_db)):
    report = get_report_by_id(db, report_id)
    if report is None:
        raise HTTPException(status_code=404, detail="Report not found")
    delete_report(db, report)
    return {"message": "Report deleted"}
