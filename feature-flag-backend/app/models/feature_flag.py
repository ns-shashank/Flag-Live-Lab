# app/models/feature_flag.py
from sqlalchemy import Column, Integer, String, Boolean, DateTime, func
from app.database import Base

class FeatureFlag(Base):
    __tablename__ = "feature_flags"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    description = Column(String, nullable=True)
    is_enabled = Column(Boolean, default=False)
    environment = Column(String, default="dev")
    created_by = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
