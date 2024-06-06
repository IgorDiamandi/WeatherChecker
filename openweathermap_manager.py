from requests import get
import streamlit as st

from location_manager import convert_timestamp_to_timezone


class OpenWeatherMapManager:
    def __init__(self, latitude, longitude, date, selected_location, timezone):
        self.api_key = '85022b8d0d20c6093a527c3ba8bb0c4f'
        self.latitude = latitude
        self.longitude = longitude
        self.date = date
        self.selected_location = selected_location
        self.timezone = timezone

    def publish_weather_data(self):
        weather_http_response = get(f"https://api.openweathermap.org/data/3.0/onecall?"
                                    f"lat={self.latitude}"
                                    f"&lon={self.longitude}"
                                    f"&exclude=hourly,daily"
                                    f"&date={self.date}"
                                    f"&units=metric&appid={self.api_key}").json()
        data_point_names = [
            'current/dt',
            'current/sunrise',
            'current/sunset',
            'current/temp',
            'current/feels_like',
            'current/pressure',
            'current/humidity',
            'current/visibility',
            'current/wind_speed']

        data_points = get_nested_value(weather_http_response, data_point_names)

        st.write(f"Current date and time at {self.selected_location} is: "
                 f"{convert_timestamp_to_timezone(data_points['current/dt'], self.timezone)}")
        st.write(f"Sunrise at: {convert_timestamp_to_timezone(data_points['current/sunrise'], self.timezone)}")
        st.write(f"Sunset at: {convert_timestamp_to_timezone(data_points['current/sunset'], self.timezone)}")
        st.write(f"Temperature: {data_points['current/temp']} °C")
        st.write(f"Feels Like: {data_points['current/feels_like']} °C")
        st.write(f"Pressure: {data_points['current/pressure']} mm")
        st.write(f"Humidity: {data_points['current/humidity']} %")
        st.write(f"Visibility: {data_points['current/visibility']} m")
        st.write(f"Wind: {data_points['current/wind_speed']} m/s")


def get_nested_value(data, keys):
    result = {}
    for key in keys:
        value = data
        for part in key.split('/'):
            try:
                value = value[part]
            except (KeyError, TypeError):
                value = f"No value was returned for {key}"
                break
        result[key] = value
    return result
