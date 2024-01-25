import openmeteo_requests

import requests_cache
from retry_requests import retry

from external.weather_lexicon import WEATHER_LEX
#from weather_lexicon import WEATHER_LEX

def form_meteo(daily_dict, lang):
    met_code_list = []
    line_temp_max = WEATHER_LEX[lang]['t_max'] + ': ' + str(daily_dict['apparent_temperature_max'])
    line_temp_min = WEATHER_LEX[lang]['t_min'] + ': ' + str(daily_dict['apparent_temperature_min'])
    met_code_list.append(daily_dict['apparent_temperature_max'])
    met_code_list.append(daily_dict['apparent_temperature_min'])
    if daily_dict['weather_code'] < 50:
        line_precip = WEATHER_LEX[lang]['precip_low']
        met_code_list.append(0)
    elif daily_dict['weather_code'] < 62:
        line_precip = WEATHER_LEX[lang]['precip_high']
        met_code_list.append(1)
    elif (daily_dict['weather_code'] < 67) or (79 < daily_dict['weather_code'] < 83):
        line_precip = WEATHER_LEX[lang]['rain']
        met_code_list.append(2)
    elif (daily_dict['weather_code'] < 80) or (daily_dict['weather_code'] in [85, 86]):
        line_precip = WEATHER_LEX[lang]['snow']
        met_code_list.append(3)
    elif daily_dict['weather_code'] > 90:
        line_precip = WEATHER_LEX[lang]['storm']
        met_code_list.append(4)
    wind = daily_dict['wind_speed_10m_max']
    line_wind = ''
    if wind < 20:
        line_wind += WEATHER_LEX[lang]['calm'] 
        met_code_list.append(0)
    elif wind < 33:
        line_wind += WEATHER_LEX[lang]['moderate'] 
        met_code_list.append(1)
    else:
        line_wind += WEATHER_LEX[lang]['windy'] 
        met_code_list.append(2)
    list_azim =[i/10 for i in list(range(225, 3600, 450))]
    wind_dir = daily_dict['wind_direction_10m_dominant']
    met_code_list.append(wind_dir)
    if (list_azim[-1] <= wind_dir < 360) or (0 <= wind_dir < list_azim[0]):
        line_wind += WEATHER_LEX[lang]['north']
    elif list_azim[0] <= wind_dir < list_azim[1]:
        line_wind += WEATHER_LEX[lang]['n-west']
    elif list_azim[1] <= wind_dir < list_azim[2]:
        line_wind += WEATHER_LEX[lang]['west']
    elif list_azim[2] <= wind_dir < list_azim[3]:
        line_wind += WEATHER_LEX[lang]['s-west']
    elif list_azim[3] <= wind_dir < list_azim[4]:
        line_wind += WEATHER_LEX[lang]['sud']
    elif list_azim[4] <= wind_dir < list_azim[5]:
        line_wind += WEATHER_LEX[lang]['s-est']
    elif list_azim[5] <= wind_dir < list_azim[6]:
        line_wind += WEATHER_LEX[lang]['est']
    elif list_azim[6] <= wind_dir < list_azim[7]:
        line_wind += WEATHER_LEX[lang]['n-est']
    output = line_temp_max + '\n' + line_temp_min + '\n' + \
             line_precip + '\n' + line_wind
    return output, met_code_list

    
def meteo_api(lat, long, lang):
    # Setup the Open-Meteo API client with cache and retry on error
    cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
    retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
    openmeteo = openmeteo_requests.Client(session = retry_session)
    url = "https://api.open-meteo.com/v1/forecast"
    temp_list = ["apparent_temperature_max", "apparent_temperature_min","weather_code",
                 "wind_speed_10m_max", "wind_direction_10m_dominant"]
    params = {
        "latitude": lat,
	    "longitude": long,
	    "daily": temp_list,
	    "timezone": "auto",
	    "forecast_days": 1
    }
    responses = openmeteo.weather_api(url, params=params)
    response = responses[0].Daily()
    daily_dict = {}
    for i in range(len(temp_list)):
        daily_dict[temp_list[i]] = round(response.Variables(i).ValuesAsNumpy()[0], 2)
    return form_meteo(daily_dict, lang)
