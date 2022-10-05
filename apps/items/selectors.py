from sqlalchemy.orm import Session

from . import models
from .schemas import Item


def get_item(db: Session, item_id: int):
    return db.query(models.Item).filter(models.Item.id == item_id).first()


def create_item(db: Session, item: Item):
    db_item = models.Item(
        name=item.name,
        price=item.price,
        is_offered=False,
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
