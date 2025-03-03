from fastapi import FastAPI, HTTPException, Query
import requests

# https://www.weather.gov/documentation/services-web-api
# https://fastapi.tiangolo.com/tutorial/

app = FastAPI()

LAT = 44.5
LON = -123.28333
nws_url = "https://api.weather.gov/gridpoints/PQR/83,61/forecast"


@app.get("/weather/")
async def get_weather(period: int = Query(0)):
    # weather query up to 14 periods
    try:
        response = requests.get(nws_url)
        response.raise_for_status()
        data = response.json()

        periods = data["properties"]["periods"]
        selected_period = periods[period]
        temperature = selected_period["temperature"]
        short_description = selected_period["shortForecast"]
        period_name = selected_period["name"]

        return {
            "period": period_name,
            "temperature": f"{temperature}°F",
            "description": short_description
        }

    except requests.exceptions.RequestException as exp:
        raise HTTPException(status_code=500, detail=str(exp))
