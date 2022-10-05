import uvicorn
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from apps.collectors.router import router as collectors
from apps.items.router import router as items
from apps.items.schemas import Item
from apps.items.selectors import create_item
from apps.universities.router import router as universities
from settings.database import SessionLocal

# main


app = FastAPI(
    title="FastAPI for New Server",
    version="v0.0.1",
    docs_url="/archon",
)

if __name__ == "__main__":
    uvicorn.run(app="main:app")


# router


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/api")
async def api_root():
    return {"message": "api root"}


app.include_router(collectors, prefix="/api/collector", tags=["collectors"])
app.include_router(items, prefix="/api/items", tags=["items"])
app.include_router(universities, prefix="/api/universities", tags=["universities"])


# database


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/items", response_model=Item)
def create_items(item: Item, db: Session = Depends(get_db)):
    db_item = create_item(db=db, item=item)
    return db_item
