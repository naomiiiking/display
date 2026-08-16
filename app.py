from clients.weather import weatherClient
from clients.news import newsClient
from PIL import Image, ImageDraw, ImageFont
from dotenv import load_dotenv
import os, time
from datetime import datetime


load_dotenv()

class App:
    def __init__(self):
        self.weather = weatherClient()
        self.news = newsClient()
        self.dimensions = (400, 300) # 4.2 Inky wHAT
        self.padding_top = 5
        self.padding_left = 10

        self.env = os.environ['ENV']
        
        self.tube_logo = Image.open("assets/tube-icon.png") # London icons created by Vitaly Gorbachev - Flaticon

    def get_greeting(self):
        current_time = (datetime.now()).hour
        if current_time < 12:
            return "Good morning"
        elif current_time < 19:
            return "Good afternoon"
        else:
            return "Good evening"

    def run(self):
        if(self.env=="pi"):
            from inky.auto import auto
        print("running...")

        while(True):
            if(self.env=="pi"):
                display = auto()

            out = Image.new("RGB", self.dimensions, (255, 255, 255))

            fnt_h1 = ImageFont.truetype("assets/arial.ttf", 30)
            fnt_txt = ImageFont.truetype("assets/arial.ttf", 20)
            fnt_date = ImageFont.truetype("assets/Arial Bold.ttf", 60)
            d = ImageDraw.Draw(out)

            greeting = self.get_greeting()
            d.text((self.padding_left, self.padding_top), F"{greeting}, Naomi", font=fnt_h1, fill=(0, 0, 0))

            ##### Weather section
            current_weather = self.weather.get_weather()
            weather_icon = Image.open(current_weather[1])
            out.paste(weather_icon, (self.padding_left, self.padding_top + 40), weather_icon)
            d.text((self.padding_left + 35, self.padding_top + 45),f"{current_weather[0][1]}", font=fnt_txt, fill=(0,0,0))

            sunrise_icon = Image.open("assets/sunrise.png")
            out.paste(sunrise_icon, (self.padding_left, self.padding_top + 70), sunrise_icon)
            d.text((self.padding_left + 35, self.padding_top + 78),f"{current_weather[0][2]}", font=fnt_txt, fill=(0,0,0))

            sunset_icon = Image.open("assets/sunset.png")
            out.paste(sunset_icon, (self.padding_left, self.padding_top + 105), sunset_icon)
            d.text((self.padding_left + 35, self.padding_top + 113),f"{current_weather[0][3]}", font=fnt_txt, fill=(0,0,0))

            ##### Date section
            current_time = datetime.now()
            day = current_time.strftime("%a")
            date = current_time.strftime("%-d")
            month = current_time.strftime("%b")
            d.text((self.padding_left + 15, self.padding_top + 180), f"{day}, {month} {date}", font=fnt_date, fill=(255, 0, 0))

            ##### News section
            #news = self.news.get_news("bbc-news", "")
            #d.multiline_text((self.padding_left, self.padding_top + 175), f"{news}", font=fnt_txt, fill=(0, 0, 0))
            #news_ai = self.news.get_news("techcrunch", "")
            #d.multiline_text((self.padding_left, self.padding_top + 235), f"{news_ai}", font=fnt_txt, fill=(0, 0, 0))

            if(self.env=="pi"):
                display.set_image(out)
                display.show()
            else:
                out.show()
            time.sleep(3600)


