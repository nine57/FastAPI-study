import uvicorn
from fastapi import FastAPI

from apps.items.router import router as item_router
from apps.users.router import router as users_router
from database import Base, engine

Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="FastAPI for New Server",
    version="v0.0.1",
    docs_url="/archon",
)

if __name__ == "__main__":
    uvicorn.run(app="main:app")


# router
@app.get(path="/", description="Server Health Check")
async def check_server():
    return {"message": "server check OK"}


app.include_router(item_router, prefix="/api/items")
app.include_router(users_router, prefix="/api/users")
