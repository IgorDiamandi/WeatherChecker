import timezonefinder as tf
import pytz
from datetime import datetime
from geopy.geocoders import Nominatim


def get_timezone_from_city(city_str):
    geolocator = Nominatim(user_agent="WeatherChecker")
    location = geolocator.geocode(city_str)

    if location:
        timezone_str = tf.TimezoneFinder().timezone_at(lng=location.longitude, lat=location.latitude)
        if timezone_str:
            return timezone_str
        else:
            return "Time zone not found for this city"
    else:
        return "Incorrect city input"


def display_date_time(user_timezone, location_timezone=None):
    user_time = datetime.now(pytz.timezone(user_timezone))

    if location_timezone:
        location_time = user_time.astimezone(pytz.timezone(location_timezone))
        formatted_location_time = location_time.strftime("%A, %B %d, %Y, %I:%M %p")
        return f"Date and time in {location_timezone}: {formatted_location_time}"


def get_latitude_and_longitude(city_str):
    geolocator = Nominatim(user_agent="WeatherChecker")
    location = geolocator.geocode(city_str)
    if location:
        latitude, longitude = location.latitude, location.longitude
        return latitude, longitude
    else:
        return "Incorrect city input"