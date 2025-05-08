# Learning getting live data from API

import requests, urllib.parse, unicodedata

def show_menu():
    print(" \n---Weather Forecast---\n")
    print("1. Check Weather")
    print("2. Exit")

def get_weather(city):
    encoded_city = urllib.parse.quote(city)
    url = f"https://wttr.in/{encoded_city}?format=j1"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        feelslike_Celsius = data['current_condition'][0]['FeelsLikeC']
        feelslike_Fahrenheit = data['current_condition'][0]['FeelsLikeF']
        humidity_percentage = data['current_condition'][0]['humidity']
        precipitation_mm = data['current_condition'][0]['precipMM']
        pressure_hPa = data['current_condition'][0]['pressure']
        temperature_Celsius = data['current_condition'][0]['temp_C']
        temperature_Fahrenheit = data['current_condition'][0]['temp_F']
        description = data['current_condition'][0]['weatherDesc'][0]['value']
        wind_direction = data['current_condition'][0]['winddir16Point']
        wind_speed_kmph = data['current_condition'][0]['windspeedKmph']

        print(f"\n📍 Weather in {city}")
        print(f"{'Description':<18}: {description}")
        print(f"{'Feels Like (C)':<18}: {feelslike_Celsius}°C")
        print(f"{'Feels Like (F)':<18}: {feelslike_Fahrenheit}°F")
        print(f"{'Temperature (C)':<18}: {temperature_Celsius}°C")
        print(f"{'Temperature (F)':<18}: {temperature_Fahrenheit}°F")
        print(f"{'Humidity':<18}: {humidity_percentage}%")
        print(f"{'Precipitation (mm)':<18}: {precipitation_mm} mm")
        print(f"{'Pressure (hPa)':<18}: {pressure_hPa} hPa")
        print(f"{'Wind Direction':<18}: {wind_direction}")
        print(f"{'Wind Speed (km/h)':<18}: {wind_speed_kmph} km/h")
        
    else:
        print("Sorry, failed to get weather data.")

# Main loop
while True:
    show_menu()
    choice = input("Choose an option(1-2): ")
    choice = unicodedata.normalize('NFKC', choice) # handles full-width input

    if choice == "1":
        city = input("Please enter your city: ").strip() # Asks user for city
        if city == "":
            city = "Tokyo"
            print("No city entered. Defaulting to Tokyo.")
        get_weather(city)
    elif choice == "2":
        print("Goodbye. See you later.")
        break
    else:
        print("Sorry, please choose only 1 or 2.")

# Notes:
# can use print(response.json()) to see the keys after "response = requests.get(url)" or

# just paste the url in browser and replace the {city} with the city you choose.