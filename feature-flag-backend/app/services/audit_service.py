from datetime import datetime
from sqlalchemy.orm import Session
from app.models.audit_log import AuditLog

def log_action(db: Session, flag_name: str, action: str, user: str = "system"):
    audit = AuditLog(flag_name=flag_name, action=action, user=user, timestamp=datetime.utcnow())
    db.add(audit)
    db.commit()