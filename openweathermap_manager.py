from requests import get
import streamlit as st
from datetime import datetime


class OpenWeatherMapManager:
    def __init__(self, latitude, longitude, date, selected_location):
        self.api_key = '85022b8d0d20c6093a527c3ba8bb0c4f'
        self.latitude = latitude
        self.longitude = longitude
        self.date = date
        self.selected_location = selected_location

    def publish_weather_data(self):
        weather_http_response = get(f"https://api.openweathermap.org/data/3.0/onecall?"
                                    f"lat={self.latitude}"
                                    f"&lon={self.longitude}"
                                    f"&exclude=hourly,daily"
                                    f"&date={self.date}"
                                    f"&units=metric&appid={self.api_key}").json()

        print(weather_http_response)

        current_time = weather_http_response['current']['dt']
        sunrise = weather_http_response['current']['sunrise']
        sunset = weather_http_response['current']['sunset']
        temp = weather_http_response['current']['temp']
        feels_like = weather_http_response['current']['feels_like']
        pressure = weather_http_response['current']['pressure']
        humidity = weather_http_response['current']['humidity']
        visibility = weather_http_response['current']['visibility']
        wind = weather_http_response['current']['wind_speed']

        st.write(f"Current date and time at {self.selected_location} is: {datetime.fromtimestamp(current_time)}")
        st.write(f"Sunrise at: {datetime.fromtimestamp(sunrise)}")
        st.write(f"Sunset at: {datetime.fromtimestamp(sunset)}")
        st.write(f"Temperature: {temp} °C")
        st.write(f"Feels Like: {feels_like} °C")
        st.write(f"Pressure: {pressure} mm")
        st.write(f"Humidity: {humidity} %")
        st.write(f"Visibility: {visibility} m")
        st.write(f"Wind: {wind} m/s")
