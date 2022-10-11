from database import get_db
from sqlalchemy.orm import Session

from . import models, schemas


def create_user_item(item: schemas.ItemCreate, user_id: int, db: Session = get_db):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
