from apps.items.router import router as item_router
from apps.schools.router import router as schools_router
from apps.users.router import router as users_router


def root_router(app):
    app.include_router(item_router, prefix="/api/items")
    app.include_router(users_router, prefix="/api/users")
    app.include_router(schools_router, prefix="/api/schools")
    return app
