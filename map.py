
import requests
import json
import urllib
import pprint

base_url = "https://maps.googleapis.com/maps/api/geocode/json?"
# AUTH_KEY = "AIzaSyC4WCo58K9lNmUpx-O9S9f-YeYmCVHPM1A"
AUTH_KEY = "AIzaSyC4WCo58K9lNmUpx-O9S9f-YeYmCVHPM1A"

parameters = {"address": "Tuscany, Italy",
              "key": AUTH_KEY}

# urllib.parse.urlencode turns parameters into url
# print(f"{base_url}{urllib.parse.urlencode(parameters)}")
r = requests.get(f"{base_url}{urllib.parse.urlencode(parameters)}")
data = json.loads(r.content)
# pprint.pprint(data)

#   ============ Get my IP address ===== ipify.org
ip = requests.get('https://api.ipify.org').text
# print('My public IP address is: {}'.format(ip))




#   ====================
