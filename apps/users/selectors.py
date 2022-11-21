from apps.items.selectors import get_items_by_owner_id
from apps.users.models import User
from sqlalchemy.orm import Session


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def get_user_list(db: Session):
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


def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()
