from sqlalchemy.orm import Session
from app.api.database.models import User, Report
from app.api.utils.datetime_utils import get_current_datetime
from sqlalchemy.orm import Session, joinedload


def create_user(db: Session, token: str, usertype: str):
    created_at = get_current_datetime()
    db_user = User(token=token, userType=usertype, created_at=created_at)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_all_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def get_all_users_with_reports(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).options(joinedload(User.reports)).offset(skip).limit(limit).all()


def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_id_with_reports(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).options(joinedload(User.reports)).first()


def get_reports_by_user(db: Session, user_id: int):
    return db.query(Report).filter(Report.user_id == user_id).all()


def get_user_by_token(db: Session, token: str):
    return db.query(User).filter(User.token == token).first()


def delete_user(db: Session, user: User):
    db.delete(user)
    db.commit()
