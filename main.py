import asyncio

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import Base, engine
from router import root_router
from secure import ALLOW_CREDENTIALS, ALLOW_HEADERS, ALLOW_METHODS, ORIGINS

# from apps.slack.services import send_slack_message
# import nest_asyncio

Base.metadata.create_all(bind=engine)

# nest_asyncio.apply()


app = FastAPI(
    title="FastAPI for New Server",
    version="v0.0.1",
    docs_url="/archon",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,
    allow_credentials=ALLOW_CREDENTIALS,
    allow_methods=ALLOW_METHODS,
    allow_headers=ALLOW_HEADERS,
)
app = root_router(app)


# router
@app.get(path="/", description="Server Health Check")
async def check_server():
    # send_slack_message(text="데일_서버_헬스체크", channel="C6491MDPG")
    return {"status": 200, "message": "server check OK"}


if __name__ == "__main__":
    uvicorn.run(app="main:app", port=8000, reload=True, loop=asyncio)
