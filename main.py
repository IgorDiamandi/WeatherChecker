import streamlit as st
from datetime import datetime
from date_time_manager import get_timezone_from_city, display_date_time, get_latitude_and_longitude
from openweathermap_manager import OpenWeatherMapManager

user_input = st.text_input("Please enter a city name:")

if user_input:
    timezone = get_timezone_from_city(user_input)
    st.write(f"Timezone: {timezone}")
    st.write(f"Current Date and Time in {user_input}: {display_date_time(timezone, timezone)}")

    latitude, longitude = get_latitude_and_longitude(user_input)
    openweathermap_manager = OpenWeatherMapManager(latitude, longitude, datetime.now())
    openweathermap_manager.publish_weather_data()


