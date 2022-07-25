#! python3
# quickWeather.py - Prints the weather for a location from the command line.
import json
from time import sleep
import requests
import sys
from pprint import pprint
# Compute location from command line arguments.
if len(sys.argv) < 2:
    print('Usage: quickWeather.py location')
    sys.exit()
location = ' '.join(sys.argv[1:])
# Download the JSON data from OpenWeatherMap.org's API.

url = "https://community-open-weather-map.p.rapidapi.com/weather"

querystring = {"q": location, "lat": "0", "lon": "0", "callback": "test",
               "id": "2172797", "lang": "null", "units": "imperial", "mode": "xml"}

headers = {
    "X-RapidAPI-Host": "community-open-weather-map.p.rapidapi.com",
    "X-RapidAPI-Key": "f63eb11c0cmshcb75fbba7169793p1b24a7jsn4726e6508cc2"
}

response = requests.request("GET", url, headers=headers, params=querystring)

pprint(response.text)

sleep(500)
