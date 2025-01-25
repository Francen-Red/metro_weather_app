import requests

ncr_cities = [ "Caloocan", "Malabon", "Navotas", "Valenzuela", "Quezon City",
    "Marikina", "Pasig", "Taguig", "Makati", "Manila",
    "Mandaluyong", "San Juan", "Pasay", "Parañaque", "Las Piñas", "Muntinlupa"]

while True:
    # Ask the user for a city
    city_name = input("Hi! Please input a city in NCR, Philippines: ")
    if city_name not in ncr_cities:  # Ask 
        print("Please input a city in NCR, Philippines only.")
        continue 