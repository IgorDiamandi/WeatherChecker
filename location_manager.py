from timezonefinder import TimezoneFinder
from geopy.geocoders import Nominatim
import pytz
from datetime import datetime


class LocationManager:
    def __init__(self, city, country, longitude, latitude):
        self.city = city
        self.country = country
        self.longitude = longitude
        self.latitude = latitude

    def get_timezone(self):
        try:
            geolocator = Nominatim(user_agent="city_timezone_finder")
            tf = TimezoneFinder()
            city_name = f"{self.city}, {self.country}"

            location = geolocator.geocode(city_name)
            if not location:
                raise ValueError(f"Could not find the city: {city_name}")

            timezone_str = tf.timezone_at(lng=location.longitude, lat=location.latitude)
            if not timezone_str:
                raise ValueError(f"Could not determine the timezone for the city: {city_name}")

            return timezone_str

        except Exception as e:
            return str(e)


def convert_timestamp_to_timezone(timestamp, timezone_str):
    try:
        pytz.timezone(timezone_str)
        if type(timestamp) is int:
            naive_datetime = datetime.utcfromtimestamp(timestamp)
            utc_datetime = pytz.utc.localize(naive_datetime)
            target_timezone = pytz.timezone(timezone_str)
            localized_datetime = utc_datetime.astimezone(target_timezone)
            return localized_datetime.strftime('%Y-%m-%d %H:%M:%S')
        else:
            return timestamp
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
