import requests
from datetime import datetime
from pprint import pprint
from config import API_KEY, CITY


def fetch_weather_data(api_key, city):
    """
    Fetch weather data from the API for a specific city.
    """
    # Endpoint URL for the weather API
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"
    try:
        # Send GET request to the API
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes

        # Parse JSON response
        data = response.json()

        location = data['location']['name']
        temperature_c = data['current']['temp_c']
        humidity = data['current']['humidity']
        pressure = data['current']['pressure_in']


        return location, temperature_c, humidity, pressure

    except requests.exceptions.RequestException as e:
        # Handle connection errors or bad responses
        print("Error fetching weather data:", e)
        return None, None, None



r = fetch_weather_data(API_KEY,CITY[0])
s = fetch_weather_data(API_KEY,CITY[1])
t = fetch_weather_data(API_KEY,CITY[2])

pprint(r)
pprint(s)
pprint(t)


# # Example usage
# api_key = 'your_api_key'
# city = 'London'

# temperature, humidity, weather_description = fetch_weather_data(api_key, city)
# if temperature is not None:
#     print(f"Temperature in {city}: {temperature}°C")
#     print(f"Humidity in {city}: {humidity}%")
#     print(f"Weather description in {city}: {weather_description}")
# else:
#     print("Failed to fetch weather data.")