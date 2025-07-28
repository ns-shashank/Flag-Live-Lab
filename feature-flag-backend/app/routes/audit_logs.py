from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.audit_log import AuditLog
from app.schemas.audit_log import AuditLogResponse
from app.database import get_db

router = APIRouter(prefix="/audit", tags=["Audit Logs"])

@router.get("/", response_model=list[AuditLogResponse])
def get_audit_logs(db: Session = Depends(get_db)):
    return db.query(AuditLog).all()