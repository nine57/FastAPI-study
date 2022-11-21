from typing import Optional

from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None


class ItemCreate(ItemBase):
    owner_id: int


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True
