import uvicorn
from fastapi import FastAPI

from apps.collectors import router as collectors
from apps.items import router as items
from apps.universities import router as universities

app = FastAPI(
    title="FastAPI for New Server",
    version="v0.0.1",
    docs_url="/archon",
)

if __name__ == "__main__":
    uvicorn.run(app="main:app")


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/api")
async def api_root():
    return {"message": "api root"}


app.include_router(collectors.router, prefix="/api/collector", tags=["collectors"])
app.include_router(items.router, prefix="/api/items", tags=["items"])
app.include_router(
    universities.router, prefix="/api/universities", tags=["universities"]
)
