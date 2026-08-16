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
        elif current_time > 12 & current_time < 19:
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
            fnt_txt = ImageFont.truetype("assets/arial.ttf", 15)
            d = ImageDraw.Draw(out)

            greeting = self.get_greeting()
            d.text((self.padding_left, self.padding_top), F"{greeting}, Naomi", font=fnt_h1, fill=(0, 0, 0))
            ##### News section
            news = self.news.get_news("bbc-news", "")
            d.multiline_text((self.padding_left, self.padding_top + 175), f"{news}", font=fnt_txt, fill=(0, 0, 0))

            #news_ai = self.news.get_news("techcrunch", "")
            #d.multiline_text((self.padding_left, self.padding_top + 235), f"{news_ai}", font=fnt_txt, fill=(0, 0, 0))

            if(self.env=="pi"):
                display.set_image(out)
                display.show()
            else:
                out.show()
            time.sleep(3600)


