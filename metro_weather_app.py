import requests

ncr_cities = [ "Caloocan", "Malabon", "Navotas", "Valenzuela", "Quezon City",
    "Marikina", "Pasig", "Taguig", "Makati", "Manila",
    "Mandaluyong", "San Juan", "Pasay", "Parañaque", "Las Piñas", "Muntinlupa"]

def fetch_weather_data(city_name):
    weather_url = "https://api.openweathermap.org/data/2.5/weather?"  # base URL to fetch data from website
    with open("api_key", "r") as file:
            api_key = file.read().strip()

    # Request Parameters
    weather_parameters = {
        "appid": api_key,
        "q": city_name + ",PH", # Append PH (Philippines) to limit search within the country
        "units": "metric",       # Display temperature in Celsius (how Filipinos display temp)
        "lang": "en"            # Display the data in English
    }
    
    # Make a request to OpenWeatherMap using requests module
        # Store in weather_response the data fetched
    weather_response = requests.get(weather_url, parameter=weather_parameters) # Use requests.get to request data from the URL with parameters 

    weather_response.raise_for_status()  # Use raise_forstatus to check the HTTP status and if there's any error encountered

    return weather_response.json()  # Use json to analyze and process the text data for easy access
 
while True:
    # Ask the user for a city
    city_name = input("Hi! Please input a city in NCR, Philippines: ")
    if city_name not in ncr_cities:  # Check if the city is valid
        print("Please input a city in NCR, Philippines only.")
        continue 