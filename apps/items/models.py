from settings.database import Base
from sqlalchemy import Boolean, Column, Float, Integer, String


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Float)
    is_offer = Column(Boolean, default=False)
