from fastapi import APIRouter
from app.services.pollution_service import get_pollution

router = APIRouter()

@router.get("/pollution/{city}")
async def pollution(city: str):
    return await get_pollution(city)