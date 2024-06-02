import streamlit as st
import json
from datetime import datetime
from location_manager import LocationManager, display_date_time, extract_city_name, find_city_by_name
from openweathermap_manager import OpenWeatherMapManager

with open('cities.json', 'r', encoding='UTF-8') as f:
    cities_data = json.load(f)

city_names = {}
for city in cities_data:
    city_name = city['name']
    country_code = city['country']
    if city_name in city_names:
        city_names[city_name].append(country_code)
    else:
        city_names[city_name] = [country_code]

cities = []
for city_name, countries in city_names.items():
    if len(countries) > 1:
        for country in countries:
            cities.append(f"{city_name} ({country})")
    else:
        cities.append(city_name)


user_input = st.selectbox("Select a city:", options=cities)


if user_input:
    city_name = extract_city_name(user_input)
    location = LocationManager(
        find_city_by_name(city_name, cities_data)['name'],
        find_city_by_name(city_name, cities_data)['country'],
        find_city_by_name(city_name, cities_data)['lat'],
        find_city_by_name(city_name, cities_data)['lng'])

    timezone = location.get_timezone()

    st.write(f"Timezone: {timezone}")
    st.write(f"Current Date and Time in {user_input}: {display_date_time(timezone, timezone)}")

    openweathermap_manager = OpenWeatherMapManager(location.latitude, location.longitude, datetime.now())
    openweathermap_manager.publish_weather_data()
