from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def index():
    """
    returns {'ok': True} if running
    """
    return {"ok": True}
