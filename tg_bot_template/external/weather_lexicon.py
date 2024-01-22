from typing import Dict

WEATHER_LEX_RU: Dict[str, str] = {
    't_max': 'Максимальная температура суток (по ощущениям)',
    't_min': 'Минимальная температура суток (по ощущениям)',
    'precip_high': 'Скорее пасмурно',
    'precip_low': 'Скорее ясно',
    'rain': 'Дождь',
    'snow': 'Снег',
    'storm': 'Гроза',
    'moderate': 'Умеренный ',
    'windy': 'Сильный ',
    'calm': 'Легкий или отсутствующий ',
    'north': 'северный ветер',
    'n-west': 'северо-западный ветер',
    'n-est': 'северо-восточный ветер',
    'west': 'западный ветер',
    'est': 'восточный ветер',
    'sud': 'южный ветер',
    's-west': 'юго-западный ветер',
    's-est': 'юго-восточный ветер'
}

WEATHER_LEX_EN: Dict[str, str] = {
    't_max': 'Maximal daily temperature (feels like)',
    't_min': 'Minimal daily temperature (feels like)',
    'precip_high': 'Overcast',
    'precip_low': 'Clear',
    'rain': 'Rainy',
    'snow': 'Snowy',
    'storm': 'Thinderstorm',
    'moderate': 'Moderate ',
    'windy': 'Strong ',
    'calm': 'Light or abcsent ',
    'north': 'north wind',
    'n-west': 'north-west wind',
    'n-est': 'north-est wind',
    'west': 'west wind',
    'est': 'wast wind',
    'sud': 'south wind',
    's-west': 'south-west wind',
    's-est': 'south-east wind'
}

WEATHER_LEX_FR: Dict[str, str] = {
    't_max': 'Temperature ressenti maximal du jour ',
    't_min': 'Temperature ressenti minimal du jour ',
    'precip_high': 'Généralement nuageux',
    'precip_low': 'Généralement clair',
    'rain': 'Plui',
    'snow': 'Neige',
    'storm': 'Tempet',
    'moderate': 'Modéré ',
    'windy': 'Fort ',
    'calm': 'Leger ou absent ',
    'north': 'vent du nord',
    'n-west': 'vent du nord-west',
    'n-est': 'vent du nord-est',
    'west': 'vent du west',
    'est': 'vent d\'est',
    'sud': 'vent du sud',
    's-west': 'vent du sud-west',
    's-est': 'vent du sud-est'
}

WEATHER_LEX: Dict[str, dict] = {'ru': WEATHER_LEX_RU, 'en': WEATHER_LEX_EN, 'fr': WEATHER_LEX_FR}