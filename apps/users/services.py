from apps.items.selectors import get_items_by_owner_id
from apps.users.models import User as db_User
from apps.users.schemas import User, UserCreate
from apps.users.selectors import get_users
from sqlalchemy.orm import Session


def create(db: Session, user: UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = db_User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    print(db_user.id)
    return db_user


def get(db: Session):
    response = list()
    db_user = get_users(db=db)
    for user in db_user:
        items = get_items_by_owner_id(db=db, owner_id=user.id, limit=3)
        user = User(
            id=user.id,
            email=user.email,
            is_active=user.is_active,
            items=items,
        )
        response.append(user)
    return response
