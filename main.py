import nest_asyncio
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from apps.items.router import router as item_router

# from apps.slack.services import send_slack_message
from apps.schools.router import router as schools_router
from apps.users.router import router as users_router
from database import Base, engine

Base.metadata.create_all(bind=engine)

nest_asyncio.apply()

app = FastAPI(
    title="FastAPI for New Server",
    version="v0.0.1",
    docs_url="/archon",
)

origins = [
    "http://localhost",
    "http://127.0.0.1",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "DELETE", "PUT"],
    allow_headers=["*"],
)


# router
@app.get(path="/", description="Server Health Check")
async def check_server():
    # send_slack_message(text="데일_서버_헬스체크", channel="C6491MDPG")
    return {"status": 200, "message": "server check OK"}


app.include_router(item_router, prefix="/api/items")
app.include_router(users_router, prefix="/api/users")
app.include_router(schools_router, prefix="/api/schools")


if __name__ == "__main__":
    uvicorn.run(app="main:app")
