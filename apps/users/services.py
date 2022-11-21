from apps.users.models import User as db_User
from apps.users.schemas import UserCreate
from sqlalchemy.orm import Session


def create_user(db: Session, user: UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = db_User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    return db_user
