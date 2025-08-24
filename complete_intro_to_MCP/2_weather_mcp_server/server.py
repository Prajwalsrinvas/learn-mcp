import httpx
from fastmcp import FastMCP

mcp = FastMCP(name="weather-server")


@mcp.tool
def get_weather(latitude: float, longitude: float) -> dict:
    """Get current weather data for a given latitude and longitude."""
    try:
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "current": [
                "temperature_2m",
                "relative_humidity_2m",
                "apparent_temperature",
                "is_day",
                "precipitation",
                "rain",
                "wind_speed_10m",
            ],
            "wind_speed_unit": "mph",
            "temperature_unit": "fahrenheit",
            "precipitation_unit": "inch",
        }

        url = "https://api.open-meteo.com/v1/forecast"

        with httpx.Client() as client:
            response = client.get(url, params=params)
            response.raise_for_status()
            data = response.json()

        current = data["current"]

        return {
            "temperature": {
                "current": current["temperature_2m"],
                "feelsLike": current["apparent_temperature"],
                "unit": "fahrenheit",
            },
            "humidity": {
                "value": current["relative_humidity_2m"],
                "unit": "percent",
            },
            "wind": {
                "speed": current["wind_speed_10m"],
                "unit": "mph",
            },
            "precipitation": {
                "total": current["precipitation"],
                "rain": current["rain"],
                "unit": "inches",
            },
            "conditions": {
                "isDay": current["is_day"] == 1,
                "dayNight": "day" if current["is_day"] == 1 else "night",
            },
        }
    except Exception as error:
        return {"error": f"Error fetching weather data: {str(error)}"}


if __name__ == "__main__":
    mcp.run()
