import requests

# Create a list of cities in Metro Manila
ncr_cities = [ "caloocan", "malabon", "navotas", "valenzuela", "quezon city",
    "marikina", "pasig", "taguig", "makati", "manila",
    "mandaluyong", "san juan", "pasay", "parañaque", "las piñas", "muntinlupa"]

# Create a dictionary of text colors using ANSII color codes 
color_codes = {
    "red": "\033[31m",
    "orange": "\033[38;5;214m",
    "yellow": "\033[33m",
    "green": "\033[32m",
    "blue": "\033[34m",
    "pink": "\033[38;5;213m",
    "violet": "\033[35m",
    "brown": "\033[38;5;94m",
    "reset_color": "\033[0m"
}

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
    try:
        # Store in weather_response the data fetched
        weather_response = requests.get(weather_url, weather_parameters) # Use requests.get to request data from the URL with parameters 
        weather_response.raise_for_status()  # Use raise_forstatus to check the HTTP status and if there's any error encountered
        return weather_response.json()  # Use json to analyze and process the text data for easy access
    except requests.exceptions.RequestException as e:
        print(f"Error: Unable to fetch weather data. {e}")
        return None


def display_weather(data):
    if not data:
        print("No data available.")
        return
    
    # Extract relevant information
    city = data.get("name")
    temp = data["main"]["temp"]
    weather_description = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]

    # Display the weather information
    print(f"{color_codes['red']}\nWeather in {city}:{color_codes['reset_color']}")
    print(f"{color_codes['orange']}Temperature:{color_codes['reset_color']} {temp}°C")
    print(f"{color_codes['yellow']}Condition:{color_codes['reset_color']} {weather_description.capitalize()}")
    print(f"{color_codes['green']}Humidity:{color_codes['reset_color']} {humidity}%")
    print(f"{color_codes['blue']}Wind Speed:{color_codes['reset_color']} {wind_speed} m/s")

while True:
    # Ask the user for a city
    city_name = input(f"{color_codes['brown']}Hi! Please input a city in NCR, Philippines:{color_codes['reset_color']} ").lower()
    if city_name not in ncr_cities:  # Check if the city is valid
        print("Please input a city in NCR, Philippines only.")
        continue 
    
    # Fetch and display the weather data
    weather_data = fetch_weather_data(city_name)
    display_weather(weather_data)

    # Ask the user if they want to input another city
    while True:
        another_city = input(f"{color_codes['pink']}Do you want to input another city? (yes/no):{color_codes['reset_color']} ").strip().lower()
        if another_city == "yes":
            break  # Restart the main loop
        elif another_city == "no":
            print("Thank you for using the weather app!")
            exit()  # Exit the program
        else:
            print("Invalid input. Please type 'yes' or 'no'.")
