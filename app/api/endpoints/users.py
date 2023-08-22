from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.api.schemas.report_schemas import Report
from app.api.database.queries.user_queries import create_user, get_user_by_token, delete_user, get_reports_by_user, \
    get_user_by_id, get_all_users, get_all_users_with_reports, get_user_by_id_with_reports
from app.api.schemas.user_schemas import UserCreate, User
from app.api.database.dependency.db_instance import get_db
from app.api.database.base import Base, engine

Base.metadata.create_all(bind=engine)

router = APIRouter()


@router.post("/register/", response_model=User)
def register_user(user_data: UserCreate, db: Session = Depends(get_db)):
    user = create_user(db, user_data.token)
    return user


@router.get("/users/", response_model=list[User])
async def get_all_users_endpoint(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = get_all_users(db, skip=skip, limit=limit)
    return users


@router.get("/users-include-reports/", response_model=list[User])
async def get_all_users_including_reports_endpoint(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = get_all_users_with_reports(db, skip=skip, limit=limit)
    return users


@router.get("/users/{token}/", response_model=User)
async def get_user_by_token_endpoint(token: str, db: Session = Depends(get_db)):
    user = get_user_by_token(db, token)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user


@router.get("/users/{user_id}/", response_model=User)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    user = get_user_by_id(db, user_id)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user


@router.get("/user-include-repors/{user_id}/", response_model=User)
async def get_user_include_report(user_id: int, db: Session = Depends(get_db)):
    user = get_user_by_id_with_reports(db, user_id)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user


@router.get("/users/{user_id}/reports/", response_model=list[Report])
async def get_user_reports(user_id: int, db: Session = Depends(get_db)):
    user_reports = get_reports_by_user(db, user_id)
    return user_reports


@router.delete("/users/{token}/")
async def delete_user_by_token(token: str, db: Session = Depends(get_db)):
    user = get_user_by_token(db, token)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    delete_user(db, user)
    return {"message": "User deleted"}
