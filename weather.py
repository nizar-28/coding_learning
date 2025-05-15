import requests, urllib.parse

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

        weather_report = f"""
📍 Weather in {city}
{'Description':<18}: {description}
{'Feels Like (C)':<18}: {feelslike_Celsius}°C
{'Feels Like (F)':<18}: {feelslike_Fahrenheit}°F
{'Temperature (C)':<18}: {temperature_Celsius}°C
{'Temperature (F)':<18}: {temperature_Fahrenheit}°F
{'Humidity':<18}: {humidity_percentage}%
{'Precipitation (mm)':<18}: {precipitation_mm} mm
{'Pressure (hPa)':<18}: {pressure_hPa} hPa
{'Wind Direction':<18}: {wind_direction}
{'Wind Speed (km/h)':<18}: {wind_speed_kmph} km/h
"""
        return weather_report
    else:
        return "Sorry, failed to get weather data."