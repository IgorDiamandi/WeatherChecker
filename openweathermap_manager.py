from requests import get


class OpenWeatherMapManager:
    def __init__(self, latitude, longitude):
        self.api_key = '85022b8d0d20c6093a527c3ba8bb0c4f'
        self.latitude = latitude
        self.longitude = longitude


    def get_weather_data(self):
        return get(f"""https://api.openweathermap.org/data/3.0/onecall?lat="
            {self.latitude}&lon={self.longitude}&appid={self.api_key}""")