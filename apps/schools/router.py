from apps.schools.selectors import get_data
from apps.schools.services import create_school_code
from database import get_db
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter(tags=["schools"])


@router.post("/code")
async def post_code(db: Session = Depends(get_db)):
    school_list = create_school_code(db=db)
    return school_list


@router.get("")
async def get_API_data(db: Session = Depends(get_db)):
    await get_data(db=db)
    return True
