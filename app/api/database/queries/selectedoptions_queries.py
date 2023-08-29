from sqlalchemy.orm import Session
from app.api.database.models import SelectedOptions
from app.api.schemas.selected_options_schemas import SelectedOptionsCreate


def create_selected_options(db: Session, rep_id: int, selectd_opt: str):
    db_selected_options = SelectedOptions(reports_id=rep_id, select_opt=selectd_opt)
    db.add(db_selected_options)
    db.commit()
    db.refresh(db_selected_options)
    return db_selected_options


def get_selected_options_by_report(db: Session, report_id: int):
    return db.query(SelectedOptions).filter(SelectedOptions.reports_id == report_id).all()
