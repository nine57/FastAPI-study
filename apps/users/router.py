from apps.users.schemas import UserCreate
from apps.users.selectors import get_user_by_id
from apps.users.serializers import user_serializer
from apps.users.services import create, get
from database import get_db
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter(tags=["users"])


@router.get("")
async def read_users(db: Session = Depends(get_db)):
    users = get(db)
    return users


@router.get("/me")
async def read_user_me(db: Session = Depends(get_db)):
    return {"username": "fakecurrentuser"}


@router.get("/{user_id}")
async def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user_by_id(db=db, user_id=user_id)
    data = user_serializer(user=db_user)
    return {"status": "success", "data": data}


@router.post("")
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = create(db=db, user=user)
    data = user_serializer(user=db_user)
    return {"status": "created", "data": data}
