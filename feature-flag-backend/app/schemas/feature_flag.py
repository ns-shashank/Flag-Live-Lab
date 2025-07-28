from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class FeatureFlagBase(BaseModel):
    name: str
    description: Optional[str] = None
    is_enabled: bool
    environment: Optional[str] = "dev"

class FeatureFlagCreate(FeatureFlagBase):
    pass

class FeatureFlagUpdate(BaseModel):
    description: Optional[str] = None
    is_enabled: Optional[bool] = None
    environment: Optional[str] = None

class FeatureFlagResponse(FeatureFlagBase):
    id: int
    created_by: Optional[str]
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True
