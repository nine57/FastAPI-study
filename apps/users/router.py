from apps.users.schemas import UserCreate
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


@router.get("/{username}")
async def read_user(username: str, db: Session = Depends(get_db)):
    return {"username": username}


@router.post("")
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    user = create(db=db, user=user)
    return user
