from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.api.database.base import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    token = Column(String(10), unique=True, index=True)
    userType = Column(String(20))
    created_at = Column(DateTime)
    reports = relationship("Report", back_populates="user")


class SelectedOptions(Base):
    __tablename__ = "selectedoptions"
    id = Column(Integer, primary_key=True, index=True)
    select_opt = Column(String(1000))
    reports_id = Column(Integer, ForeignKey("reports.id"))

    rep = relationship("Report", back_populates="selectedoptions")

class Report(Base):
    __tablename__ = "reports"
    id = Column(Integer, primary_key=True, index=True)
    qualitative = Column(String(500))
    quantitative = Column(String(500))
    selected_report = Column(String(20))  # Corrected type
    comment = Column(String(500))
    agree = Column(Boolean)
    created_at = Column(DateTime, default=datetime.utcnow)  # Automatic timestamp
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="reports")
    selectedoptions = relationship("SelectedOptions", back_populates="rep")
