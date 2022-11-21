from apps.items import models
from sqlalchemy.orm import Session


def get_item_list(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def get_items_by_owner_id(db: Session, owner_id: int, skip: int = 0, limit: int = 100):
    return (
        db.query(models.Item)
        .filter(models.Item.owner_id == owner_id)
        .offset(skip)
        .limit(limit)
        .all()
    )
