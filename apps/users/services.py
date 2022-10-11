from apps.users.models import User as db_User
from apps.users.schemas import User, UserCreate
from apps.users.selectors import get_users
from sqlalchemy.orm import Session


def create(db: Session, user: UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = db_User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    return db_user


def get(db: Session):
    response = list()
    db_user = get_users(db=db)
    for user in db_user:
        user = User(
            id=user.id,
            email=user.email,
            is_active=user.is_active,
        )
        response.append(user)
    return response
