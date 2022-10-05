from apps.items.schemas import Item
from fastapi import APIRouter

router = APIRouter()


@router.post("")
async def create_item(item: Item):
    item.name + item.price
    return item


@router.get("/{item_id}")
async def item(item_id: int, query: str = None, boolean: bool = True):
    return {"message": (item_id, query, boolean)}
