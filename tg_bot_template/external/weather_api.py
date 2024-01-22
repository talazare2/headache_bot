import openmeteo_requests

import requests_cache
import pandas as pd
from retry_requests import retry

def feels_like(responses):
    response = responses[0]
    print(response)




def meteo(lat, long):
    # Setup the Open-Meteo API client with cache and retry on error
    cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
    retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
    openmeteo = openmeteo_requests.Client(session = retry_session)
    url = "https://api.open-meteo.com/v1/forecast"
    temp_list = ["apparent_temperature_max", "apparent_temperature_min",
                 "precipitation_probability_mean", "weather_code",
                 "wind_speed_10m_max", "wind_direction_10m_dominant"]
    params = {
        "latitude": lat,
	    "longitude": long,
	    "daily": temp_list,
	    "timezone": "auto",
	    "forecast_days": 1
    }
    responses = openmeteo.weather_api(url, params=params)
    output_weather = feels_like(responses)
    return output_weather

meteo(43.75, 5.88)