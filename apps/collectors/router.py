from fastapi import APIRouter

router = APIRouter()


@router.get("/{collect_id}")
async def collect(collect_id: int):
    return {"message": collect_id}
