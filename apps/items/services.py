from sqlalchemy.orm import Session

from . import models, schemas


def create_item(item: schemas.ItemCreate, db: Session):
    db_item = models.Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
