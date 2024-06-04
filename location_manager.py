import timezonefinder as tf
import pytz
from datetime import datetime
from geopy.geocoders import Nominatim


class LocationManager:
    def __init__(self, city, country, longitude, latitude):
        self.city = city
        self.country = country
        self.longitude = longitude
        self.latitude = latitude

    def get_timezone(self):
        geolocator = Nominatim(user_agent="WeatherChecker")
        location = geolocator.geocode(self.city)

        if location:
            timezone_str = tf.TimezoneFinder().timezone_at(lng=float(self.longitude), lat=float(self.latitude))
            if timezone_str:
                return timezone_str
            else:
                return "Time zone not found for this city"
        else:
            return "Incorrect city input"


def get_local_time(timezone_str):
    try:
        timezone = pytz.timezone(timezone_str)
        current_time = datetime.now(timezone)
        return current_time.strftime('%Y-%m-%d %H:%M:%S %Z%z')
    except pytz.UnknownTimeZoneError:
        return f"Unknown timezone: {timezone_str}"


def extract_city_name(city_with_country):
    if '(' in city_with_country and ')' in city_with_country:
        pos = city_with_country.index('(')
        city_name = city_with_country[:pos].strip()
        return city_name
    else:
        return city_with_country


def find_city_by_name(city_name, data):
    for city_node in data:
        if city_node['name'] == city_name:
            return city_node
    return None
