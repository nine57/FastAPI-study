from apps.users.schemas import User
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# TODO Token 연결
def fake_decode_token(token):
    return User(id=1, email="test@test.com")


async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    return user
