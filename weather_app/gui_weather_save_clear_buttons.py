import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests, urllib.parse, io, os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def get_weather():
    city = city_entry.get().strip()
    if city == "":
        city = "Tokyo"
        messagebox.showinfo("Notice", "No city entered. Defaulting to Tokyo.")

    encoded_city = urllib.parse.quote(city)
    url = f"https://wttr.in/{encoded_city}?format=j1"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code != 200:
            raise Exception("Sorry, failed to get data.")
        
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
        icon_url = data['current_condition'][0]['weatherIconUrl'][0]['value']

        result = f"""
🈁 Weather in {city}
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
        result_text.config(state="normal")
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, result)
        result_text.config(state="disabled")

        # Load and display icon
        if icon_url.startswith("http"):
            icon_response = requests.get(icon_url)
            img_data = icon_response.content
            img = Image.open(io.BytesIO(img_data)).resize((64, 64))
            icon = ImageTk.PhotoImage(img)
            icon_label.config(image=icon)
            icon_label.image = icon

        else:
            icon_label.config(image="")

    except Exception as e:
        messagebox.showerror("Error", "Sorry, failed to fetch weather data.\n" + str(e))

def save_result():
    result = result_text.get("1.0", tk.END).strip()
    if not result:
        messagebox.showinfo("Info", "Nothing to save.")
        return
    
    try:
        with open(os.path.join(BASE_DIR, "weather_log.txt"), "a", encoding="utf-8") as file:
            file.write(result + "\n" + "-"*40 + "\n")
        messagebox.showinfo("Saved", "Weather saved to 'weather_log.txt'.")
    
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save file.\n{e}")

def clear_result():
    result_text.config(state="normal")
    result_text.delete("1.0", tk.END)
    result_text.config(state="disabled")
    icon_label.config(image="")
    icon_label.image = None
    city_entry.delete(0, tk.END)

# Create the GUI window
root = tk.Tk()
root.title("Weather Forecast")
root.geometry("450x400")

# Input field
city_entry = tk.Entry(root, font=("Arial", 14))
city_entry.pack(pady=10)

# Weather icon placeholder
icon_label = tk.Label(root)
icon_label.pack()

# Scrollable output area
result_frame = tk.Frame(root)
result_frame.pack(padx=10, pady=5, fill="both", expand=True)

scrollbar = tk.Scrollbar(result_frame)
scrollbar.pack(side="right", fill="y")

result_text = tk.Text(result_frame, wrap="word", font=("Courier", 10), yscrollcommand=scrollbar.set, height=10)
result_text.pack(side="left", fill="both", expand=True)
result_text.config(state="disabled")
scrollbar.config(command=result_text.yview)

# Button
get_button = tk.Button(root, text="Get Weather", font=("Arial", 12), command=get_weather)
get_button.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=5)

save_button = tk.Button(button_frame, text="💾 Save", font=("Arial", 10), command=save_result)
save_button.pack(side="left", padx=10)

clear_button = tk.Button(button_frame, text="🧹 Clear", font=("Arial", 10), command=clear_result)
clear_button.pack(side="left", padx=10)

# Start the main loop
root.mainloop()