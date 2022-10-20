from pydantic import BaseModel


class SchoolCodeBase(BaseModel):
    code: str
    regulator: str
    type: str
