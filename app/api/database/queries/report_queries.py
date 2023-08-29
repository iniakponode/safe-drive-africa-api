from sqlalchemy.orm import Session, joinedload
from app.api.database.models import Report, User
from app.api.utils.datetime_utils import get_current_datetime


def create_report(db: Session, user_id: int, qualitative: str, quantitative: str, selected_report: str, comment: str,
                  agree: bool):
    created_at = get_current_datetime()
    db_report = Report(
        user_id=user_id,
        qualitative=qualitative,
        quantitative=quantitative,
        selected_report=selected_report,
        comment=comment,
        agree=agree,
        created_at=created_at
    )
    db.add(db_report)
    db.commit()
    db.refresh(db_report)
    return db_report


async def get_reports(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Report).offset(skip).limit(limit).all()


# def get_all_selected_options_for_reports(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(Report).options(joinedload(Report.selected_re)).offset(skip).limit(limit).all()


def get_report_by_id(db: Session, report_id: int):
    return db.query(Report).filter(Report.id == report_id).first()


def get_reports_by_id_with_selections(db: Session, report_id: int):
    return db.query(Report).filter(Report.id == report_id).options(joinedload(User.reports)).first()


def delete_report(db: Session, report: Report):
    db.delete(report)
    db.commit()
