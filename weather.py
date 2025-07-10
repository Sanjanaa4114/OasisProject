import requests

def get_weather(city, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        weather = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"]
        }
        return weather
    else:
        return None

def main():
    print("🌦️  Simple Weather App")
    api_key = input("Enter your OpenWeatherMap API key: ")
    city = input("Enter city name: ")

    weather = get_weather(city, api_key)

    if weather:
        print(f"\n📍 Weather in {weather['city']}:")
        print(f"🌡️ Temperature: {weather['temperature']}°C")
        print(f"💧 Humidity: {weather['humidity']}%")
        print(f"🌤️ Condition: {weather['description'].title()}")
    else:
        print("❌ Failed to retrieve weather. Please check the city name or API key.")

if __name__ == "__main__":
    main()
