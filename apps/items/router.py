from typing import List

from apps.items.schemas import Item, ItemCreate
from apps.items.selectors import get_items
from apps.items.services import create_user_item
from database import get_db
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter(tags=["items"])


@router.post("")
async def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    item = create_user_item(item=item, user_id=1, db=db)
    return item


@router.get("/{item_id}")
async def item(item_id: int, query: str = None, boolean: bool = True):
    return {"message": (item_id, query, boolean)}


@router.get("", response_model=List[Item])
async def read_items(skip: int = 0, limit: int = 100):
    items = get_items(skip=skip, limit=limit)
    return items
