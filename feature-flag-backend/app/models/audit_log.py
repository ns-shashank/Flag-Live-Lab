from sqlalchemy import Column, Integer, String, DateTime
from app.database import Base

class AuditLog(Base):
    __tablename__ = "audit_logs"
    id = Column(Integer, primary_key=True, index=True)
    flag_name = Column(String, nullable=False)
    action = Column(String, nullable=False)
    user = Column(String, nullable=False)
    timestamp = Column(DateTime, nullable=False)
