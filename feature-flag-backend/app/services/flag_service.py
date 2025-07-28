from sqlalchemy.orm import Session
from app import models, schemas
from app.database import redis_client

def get_flags(db: Session):
    return db.query(models.FeatureFlag).all()

def get_flag_by_name(db: Session, name: str):
    return db.query(models.FeatureFlag).filter(models.FeatureFlag.name == name).first()

def create_flag(db: Session, flag: schemas.FeatureFlagCreate, user: str = "system"):
    db_flag = models.FeatureFlag(**flag.dict(), created_by=user)
    db.add(db_flag)
    db.commit()
    db.refresh(db_flag)
    redis_client.set(db_flag.name, db_flag.is_enabled)
    return db_flag

def update_flag(db: Session, db_flag: models.FeatureFlag, flag_update: schemas.FeatureFlagUpdate):
    for key, value in flag_update.dict(exclude_unset=True).items():
        setattr(db_flag, key, value)
    db.commit()
    db.refresh(db_flag)
    redis_client.set(db_flag.name, db_flag.is_enabled)
    return db_flag

def delete_flag(db: Session, db_flag: models.FeatureFlag):
    redis_client.delete(db_flag.name)
    db.delete(db_flag)
    db.commit()