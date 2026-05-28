from fastapi import APIRouter
from app.services.weather_service import get_weather

router = APIRouter()

@router.get("/weather/{city}")
async def weather(city: str):
    return await get_weather(city)