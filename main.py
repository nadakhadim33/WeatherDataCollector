import requests
import csv
import os
import pandas as pd

api_key = "d9f35c2a71312404a08ae2bfbad61ecb"

def save_to_csv(data):
    file_name = "weather_data.csv"
    file_exists = os.path.isfile(file_name)
    with open(file_name, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["City", "Temperature", "Feels Like", "Weather", "Humidity", "Wind Speed"])
        writer.writerow(data)

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        row = [
            data["name"],
            data["main"]["temp"],
            data["main"]["feels_like"],
            data["weather"][0]["description"],
            data["main"]["humidity"],
            data["wind"]["speed"]
        ]
        save_to_csv(row)
        print(f"Data for {city} saved successfully!")
    except requests.exceptions.HTTPError:
        print(f"City '{city}' not found. Please enter a valid city.")
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to API: {e}")

while True:
    city = input("Enter a city name (or type 'exit' to quit): ")
    if city.lower() == "exit":
        break
    get_weather(city)

df = pd.read_csv("weather_data.csv")
print("\nCurrent Weather Data:")
print(df)
