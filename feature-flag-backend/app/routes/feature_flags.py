from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, services
from app.database import get_db
from app.services import audit_service

router = APIRouter(prefix="/flags", tags=["Feature Flags"])

@router.get("/", response_model=list[schemas.FeatureFlagResponse])
def list_flags(db: Session = Depends(get_db)):
    return services.flag_service.get_flags(db)

@router.post("/", response_model=schemas.FeatureFlagResponse)
def create_flag(flag: schemas.FeatureFlagCreate, db: Session = Depends(get_db)):
    if services.flag_service.get_flag_by_name(db, flag.name):
        raise HTTPException(status_code=400, detail="Flag already exists")
    new_flag = services.flag_service.create_flag(db, flag)
    audit_service.log_action(db, flag.name, "created")
    return new_flag

@router.put("/{name}", response_model=schemas.FeatureFlagResponse)
def update_flag(name: str, flag_update: schemas.FeatureFlagUpdate, db: Session = Depends(get_db)):
    db_flag = services.flag_service.get_flag_by_name(db, name)
    if not db_flag:
        raise HTTPException(status_code=404, detail="Flag not found")
    updated_flag = services.flag_service.update_flag(db, db_flag, flag_update)
    audit_service.log_action(db, name, "updated")
    return updated_flag

@router.delete("/{name}")
def delete_flag(name: str, db: Session = Depends(get_db)):
    db_flag = services.flag_service.get_flag_by_name(db, name)
    if not db_flag:
        raise HTTPException(status_code=404, detail="Flag not found")
    services.flag_service.delete_flag(db, db_flag)
    audit_service.log_action(db, name, "deleted")
    return {"detail": "Flag deleted"}