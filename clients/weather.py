import os, requests, time
from dotenv import load_dotenv
import operator

load_dotenv()

class weatherClient:
    def __init__(self):
        self.api_key = os.environ["WEATHER_API_KEY"]
        self.lat = os.environ["LAT"]
        self.long = os.environ["LONG"]
        self.url = f"https://api.openweathermap.org/data/2.5/weather?lat={self.lat}&lon={self.long}&appid={self.api_key}&units=metric"

    def get_icon(self, description):

        icons = [
            ("rain", "assets/heavy-rain.png"),  # Icon by Apien
            ("clear", "assets/sun.png"), # Icon by Good Ware
            ("thunderstorm", "assets/thunderstorm.png"),  # Icon by Slidicon
            ("snow", "assets/snowflake.png"), # Icon by Manific
            ("clouds", "assets/cloudy-day.png") # Icon by Manific
        ]
        weather_icon = [icon for icon in icons if operator.contains(description, icon[0])]

        if len(weather_icon) == 0:
            weather_icon = [("", "assets/fallback.png")]

        return weather_icon[0][1]
    
    def get_weather(self):
        try:
            resp = requests.get(self.url)
            resp.raise_for_status

            weather = (resp.json()).get("weather")[0]
            description = weather.get('description')

            main = (resp.json()).get("main")
            temp = main.get("feels_like")

            wind = (resp.json()).get("wind")
            speed = wind.get("speed")
            deg = wind.get("deg")

            sys = (resp.json()).get("sys")
            sunrise = time.strftime(('%H:%M'), time.gmtime(int(sys.get("sunrise"))))
            sunset = time.strftime(('%H:%M'), time.gmtime(int(sys.get("sunset"))))

            location = (resp.json()).get("name")

            icon = self.get_icon(description)
            output = [f"Weather for {location}:", 
                      f"{description.capitalize()} and feels like {temp}°C",
                      f"Sunrise: {sunrise}",
                      f"Sunset: {sunset}"]
            return output, icon
        except requests.RequestException as e:
            return f"Error fetching weather data: {e}"