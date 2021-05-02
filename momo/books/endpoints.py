from fastapi import APIRouter

router = APIRouter()

@router.get("/books")
async def index():
    return { "books": "1234" }
