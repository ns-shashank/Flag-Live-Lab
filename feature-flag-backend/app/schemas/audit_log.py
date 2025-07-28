from pydantic import BaseModel
from datetime import datetime

class AuditLogResponse(BaseModel):
    id: int
    flag_name: str
    action: str
    user: str
    timestamp: datetime

    class Config:
        orm_mode = True