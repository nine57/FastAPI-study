from apps.users.models import User as db_User


def user_serializer(user: db_User):
    user_dict = {
        "id": user.id,
        "status": "Active" if user.is_active else "Not_In_Use",
    }
    return user_dict
