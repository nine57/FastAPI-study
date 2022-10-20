from database import Base
from sqlalchemy import Column, Integer, String


class SchoolCode(Base):
    __tablename__ = "school_codes"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, index=True)
    regulator = Column(String(5))
    type = Column(String(3))
