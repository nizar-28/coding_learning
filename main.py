import unicodedata
from weather import get_weather

def show_menu():
    print("\n--- Weather Forecast ---\n")
    print("1. Check Weather")
    print("2. Exit")

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
        # with open(f"{city.replace(' ', '_')}_weather.txt", "w", encoding="utf-8") as file:
        #     file.write(result)

    elif choice == "2":
        print("Goodbye. See you later.")
        break
    else:
        print("Sorry, please choose only 1 or 2.")