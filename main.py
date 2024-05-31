from date_time_manager import get_timezone_from_city, display_date_time, get_latitude_and_longitude
from openweathermap_manager import OpenWeatherMapManager
import pandas as pd

user_input = input("Please enter a city name: ")
print(get_timezone_from_city(user_input))
print(display_date_time(get_timezone_from_city(user_input), get_timezone_from_city(user_input)))

latitude, longitude = get_latitude_and_longitude(user_input)
openweathermap_manager = OpenWeatherMapManager(latitude, longitude)

weather_http_response = openweathermap_manager.get_weather_data()
current_df = pd.json_normalize(weather_http_response.json()['current'])
print(current_df)
