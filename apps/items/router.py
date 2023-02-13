from typing import List

from apps.items.schemas import Item, ItemCreate
from apps.items.selectors import get_item_list
from apps.items.services import create_item
from database import get_db
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter(tags=["items"])


@router.post("")
async def item_create(item: ItemCreate, db: Session = Depends(get_db)):
    item = await create_item(item=item, db=db)
    return item


@router.get("/{item_id}")
async def item_retrieve(item_id: int, query: str = None, boolean: bool = True):
    return {"message": (item_id, query, boolean)}


@router.get("", response_model=List[Item])
async def item_list(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = await get_item_list(db=db, skip=skip, limit=limit)
    return items
