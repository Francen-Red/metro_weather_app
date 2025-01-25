import requests

ncr_cities = [ "Caloocan", "Malabon", "Navotas", "Valenzuela", "Quezon City",
    "Marikina", "Pasig", "Taguig", "Makati", "Manila",
    "Mandaluyong", "San Juan", "Pasay", "Parañaque", "Las Piñas", "Muntinlupa"]

def fetch_weather_data(city_name):
    weather_url = "https://api.openweathermap.org/data/2.5/weather?"  # base URL to fetch data from website
    with open("api_key", "r") as file:
            api_key = file.read().strip()

    while True:
        # Ask the user for a city
        city_name = input("Hi! Please input a city in NCR, Philippines: ")
        if city_name not in ncr_cities:  # Check if the city is valid
            print("Please input a city in NCR, Philippines only.")
            continue 