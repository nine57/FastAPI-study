from typing import Union

from pydantic import BaseModel


class Item(BaseModel):
    name: str
    price: Union[float, None] = None
    is_offer: bool = False

    class Config:
        orm_mode = True
