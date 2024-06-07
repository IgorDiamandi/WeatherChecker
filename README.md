#	WeatherChecker
	Project by Igor Diamandi

	Overview:
		WeatherChecker is an application that allows users to retrieve the current weather forecast by inputting a desired location. 
		This application is based on data provided by the OpenWeatherMap service.

	Features:
		WeatherChecker provides the following information for a chosen city:
			Time zone
			Current local time
			Local sunrise and sunset times
			Actual temperature
			"Feels like" temperature
			Pressure
			Humidity
			Visibility
			Wind speed

	Functionality:
		WeatherChecker displays all available information by applying a "best effort" approach. 
		If a specific data point is unavailable from OpenWeatherMap at the time of retrieval, 
		an error message will be displayed for that data point.

	User Input:
		Users can input a city name into the "Select a city" combo selector control. 
		This control supports autosuggestions and will display available city names as the user types. If a non-existent city name is provided, a default city will be selected.

	Modules:
		cities.json: Stores all available city and country names.

		LocationManager: Contains the LocationManager class with properties for
		city, country, longitude, and latitude. This module includes functions and methods for time zone and location operations.

		OpenWeatherMapManager: Responsible for retrieving weather data from OpenWeatherMap and publishing it.

	Executable: 
		The main script is main.py.

	Known Bugs and Limitations:
		WeatherChecker uses the geopy.geocoders library for geolocation services. 
		Calls to this service in conjunction with Streamlit can fail due to timeouts. 
		A retry mechanism has been introduced to address this issue, but it is not a foolproof solution.