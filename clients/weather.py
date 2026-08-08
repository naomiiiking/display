import os, requests, time
from dotenv import load_dotenv

load_dotenv()

class weatherClient:
    def __init__(self):
        self.api_key = os.environ["WEATHER_API_KEY"]
        self.lat = os.environ["LAT"]
        self.long = os.environ["LONG"]
        self.url = f"https://api.openweathermap.org/data/2.5/weather?lat={self.lat}&lon={self.long}&appid={self.api_key}&units=metric"

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

            output = f"""
            Weather for {location}:
            \n {description.capitalize()} and feels like {temp}°C
            \n Wind speed {speed}m/s in direction °{deg}
            \n Sunrise: {sunrise}
            \n Sunset: {sunset}
            """
            print(output)
        except requests.RequestException as e:
            print(f"Error fetching data: {e}")