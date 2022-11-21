from apps.users.schemas import User, UserCreate
from apps.users.selectors import get_user_by_id, get_user_list
from apps.users.serializers import user_serializer
from apps.users.services import create_user
from apps.users.utils import get_current_user
from database import get_db
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter(tags=["users"])


@router.get("")
async def user_list(db: Session = Depends(get_db)):
    users = get_user_list(db=db)
    return users


@router.get("/me")
async def user_retrieve_for_me(
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    db_user = get_user_by_id(db=db, user_id=user.id)
    data = user_serializer(user=db_user)
    return {"status": "success", "data": data}


@router.get("/{user_id}")
async def user_retrieve(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user_by_id(db=db, user_id=user_id)
    data = user_serializer(user=db_user)
    return {"status": "success", "data": data}


@router.post("")
async def user_create(user: UserCreate, db: Session = Depends(get_db)):
    db_user = create_user(db=db, user=user)
    data = user_serializer(user=db_user)
    return {"status": "created", "data": data}


# TODO Token 연결
# @router.post("/signin")
# async def login(sns_type: SnsType, user_info: models.UserRegister):
#     if sns_type == SnsType.email:
#         is_exist = await is_email_exist(user_info.email)
#         if not user_info.email or not user_info.pw:
#             return JSONResponse(status_code=400, content=dict(msg="Email and PW must be provided'"))
#         if not is_exist:
#             return JSONResponse(status_code=400, content=dict(msg="NO_MATCH_USER"))
#         user = Users.get(email=user_info.email)
#         is_verified = bcrypt.checkpw(user_info.pw.encode("utf-8"), user.pw.encode("utf-8"))
#         if not is_verified:
#             return JSONResponse(status_code=400, content=dict(msg="NO_MATCH_USER"))
#         token = dict(
#             Authorization=f"Bearer {create_access_token(data=UserToken.from_orm(user).dict(exclude={'pw', 'marketing_agree'}),)}")
#         return token
#     return JSONResponse(status_code=400, content=dict(msg="NOT_SUPPORTED"))
