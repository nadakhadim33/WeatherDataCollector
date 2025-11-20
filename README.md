# WeatherDataCollector
# Weather Data Collector using OpenWeather API

This project collects weather data for cities entered by the user using the OpenWeather API and saves it into a CSV file (`weather_data.csv`). Users can continuously input city names, and the program handles invalid names gracefully.

## Features

* Collects temperature, feels-like temperature, weather description, humidity, and wind speed for each city.
* Saves data into a CSV file automatically.
* Allows multiple city entries in one session.
* Handles errors if a city is not found or API connection fails.

## How to Run

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Open `main.py` and run the script.
3. Enter city names when prompted. Type `exit` to stop the program.
4. All data will be saved in `weather_data.csv`.

## Requirements

* Python 3.x
* `requests`
* `pandas`

## Author

Nada Khadim Al-Balushi
AI & Data Engineering Student
Jordan
