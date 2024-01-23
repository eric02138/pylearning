import requests
import json
from pprint import pprint as pp

response = requests.get('https://api.weather.gov/points/42.8732,-71.4736')
# print(response)
# print(response.text)

dd = json.loads(response.text)
properties = dd.get('properties')
forecast_url = properties.get('forecast')
#print(forecast_url)

response2 = requests.get(forecast_url)
weather = json.loads(response2.text)
#pp(weather)

periods = weather.get('properties').get('periods')

first_three_periods = periods[0:6]
#pp(first_three_periods)

is_snow_coming = False

for period in first_three_periods:
    short_forecast = period.get("shortForecast")
    if "snow" in short_forecast.lower():
        is_snow_coming = True
        #print("DON'T RUN THE RLMS!")
    else:
        pass
        #print("Yeah, go ahead I guess.")

if is_snow_coming:
    print("DON'T RUN THE RLMS!")
else:
    print("Yeah, go ahead I guess.")