import os
import httpx
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

GEO_URL = "http://api.openweathermap.org/geo/1.0/direct"
POLLUTION_URL = "http://api.openweathermap.org/data/2.5/air_pollution"


async def get_pollution(city: str):

    async with httpx.AsyncClient() as client:

        geo_response = await client.get(
            GEO_URL,
            params={
                "q": city,
                "limit": 1,
                "appid": API_KEY
            }
        )

        geo_data = geo_response.json()

        if not geo_data:
            return {"error": "City not found"}

        lat = geo_data[0]["lat"]
        lon = geo_data[0]["lon"]

        pollution_response = await client.get(
            POLLUTION_URL,
            params={
                "lat": lat,
                "lon": lon,
                "appid": API_KEY
            }
        )

        pollution_data = pollution_response.json()

        components = pollution_data["list"][0]["components"]
        aqi = pollution_data["list"][0]["main"]["aqi"]

        return {
            "city": city,
            "aqi": aqi,
            "components": components,
            "coordinates": {
                "latitude": lat,
                "longitude": lon
            }
        }