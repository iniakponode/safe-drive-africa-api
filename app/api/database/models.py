from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.api.database.base import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    token = Column(String(10), unique=True, index=True)
    created_at = Column(DateTime)
    reports = relationship("Report", back_populates="user")


class Report(Base):
    __tablename__ = "reports"
    id = Column(Integer, primary_key=True, index=True)
    qualitative = Column(String(500))
    quantitative = Column(String(500))
    selected_report = Column(String(500))
    comment = Column(String(500))
    agree = Column(Boolean)
    created_at = Column(DateTime)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="reports")
