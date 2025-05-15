import unicodedata
from weather import get_weather
from datetime import datetime

def show_menu():
    print("\n--- Weather Forecast ---\n")
    print("1. Check Weather")
    print("2. View Saved Reports")
    print("3. Exit")

# Main loop
while True:
    show_menu()
    choice = input("Choose an option(1-2): ")
    choice = unicodedata.normalize('NFKC', choice)

    if choice == "1":
        city = input("Please enter your city: ").strip()
        if city == "":
            city = "Tokyo"
            print("No city entered. Defaulting to Tokyo.")

        result = get_weather(city)
        print(result)

        # Optional: Save to file
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        filename = "weather_history.txt"

        entry = f"""
============================
📅 Time: {now}
🈁 City: {city}
{result}
"""

        # Append to file
        with open(filename, "a", encoding="utf-8") as file:
            file.write(entry)

        print(f"✅ Weather for {city} saved to {filename}")

    elif choice == "2":
        try:
            with open("weather_history.txt", "r", encoding="utf-8") as file:
                print("\n 📂 Saved Weather Reports:")
                print(file.read())
        except FileNotFoundError:
            print("Sorry, no saved reports found yet.")

    elif choice == "3":
        print("Goodbye. See you later.")
        break
    else:
        print("Sorry, please choose only 1 or 2.")