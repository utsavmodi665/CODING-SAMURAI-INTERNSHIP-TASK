"""
Weather App Using API
Description: A weather application that fetches data from the Open-Meteo
API and displays the current weather for a specific location.
Skills: API handling, JSON parsing, error handling.
"""

import requests


def get_weather_description(code):
    """Converts WMO weather code to a human-readable string."""
    codes = {
        0: "☀️ Clear sky",
        1: "🌤️ Mainly clear",
        2: "🌥️ Partly cloudy",
        3: "☁️ Overcast",
        45: "🌫️ Fog",
        48: "🌫️ Depositing rime fog",
        51: "💧 Drizzle: Light intensity",
        53: "💧 Drizzle: Moderate intensity",
        55: "💧 Drizzle: Dense intensity",
        61: "🌧️ Rain: Slight intensity",
        63: "🌧️ Rain: Moderate intensity",
        65: "🌧️ Rain: Heavy intensity",
        71: "❄️ Snow fall: Slight intensity",
        73: "❄️ Snow fall: Moderate intensity",
        75: "❄️ Snow fall: Heavy intensity",
        80: "🌦️ Rain showers: Slight",
        81: "🌦️ Rain showers: Moderate",
        82: "🌦️ Rain showers: Violent",
        95: "⛈️ Thunderstorm",
        96: "⛈️ Thunderstorm with slight hail",
        99: "⛈️ Thunderstorm with heavy hail",
    }
    return codes.get(code, "Unknown weather condition")


def get_weather(city):
    """
    Fetches weather data for a city.

    Returns a dictionary with weather data or a dictionary with an error message.
    """
    try:
        # Step 1: Get latitude & longitude using geocoding API
        geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
        geo_response = requests.get(geo_url)
        geo_response.raise_for_status()  # Raise an exception for bad status codes
        geo_data = geo_response.json()

        if not geo_data.get("results"):
            return {"error": f"City '{city}' not found. Please check the spelling."}

        location = geo_data["results"][0]
        lat = location["latitude"]
        lon = location["longitude"]
        display_name = location.get("name", city)

        # Step 2: Get weather using latitude & longitude
        weather_url = (
            f"https://api.open-meteo.com/v1/forecast?"
            f"latitude={lat}&longitude={lon}&current_weather=true"
        )
        weather_response = requests.get(weather_url)
        weather_response.raise_for_status()
        weather_data = weather_response.json()

        current = weather_data["current_weather"]

        return {
            "city": display_name,
            "temperature": current["temperature"],
            "windspeed": current["windspeed"],
            "description": get_weather_description(current["weathercode"]),
        }

    except requests.exceptions.RequestException as e:
        return {"error": f"A network error occurred: {e}"}
    except (KeyError, IndexError):
        return {"error": "Failed to parse API response. The data format may have changed."}


def main():
    """Main function to run the weather application."""
    print("=" * 40)
    print("        WEATHER APP")
    print("=" * 40)
    while True:
        city = input("\nEnter city name (or type 'exit' to quit): ").strip()

        if city.lower() == "exit":
            print("Exiting Weather App...")
            break

        weather_info = get_weather(city)

        print("-" * 25)
        if "error" in weather_info:
            print(f"Error: {weather_info['error']}")
        else:
            print(f"Weather in {weather_info['city']}:")
            print(f"  -> Condition:   {weather_info['description']}")
            print(f"  -> Temperature: {weather_info['temperature']}°C")
            print(f"  -> Wind Speed:  {weather_info['windspeed']} km/h")
        print("-" * 25)


if __name__ == "__main__":
    main()