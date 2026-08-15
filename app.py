from clients.tfl import tflClient
from clients.weather import weatherClient
from clients.spotify import spotifyClient
from clients.news import newsClient
from PIL import Image, ImageDraw, ImageFont
from dotenv import load_dotenv
import os, time

load_dotenv()

class App:
    def __init__(self):
        self.tfl = tflClient()
        self.weather = weatherClient()
        self.spotify = spotifyClient()
        self.news = newsClient()
        self.dimensions = (400, 300) # 4.2 Inky wHAT
        self.padding_top = 5
        self.padding_left = 10

        self.env = os.environ['ENV']
        if(self.env=="pi"):
            from inky.auto import auto

        self.tube_logo = Image.open("assets/tube-icon.png") # London icons created by Vitaly Gorbachev - Flaticon
    def run(self):
        print("running...")
        #weather.get_weather()
        #spotify.get_playback()
        while(True):
            if(self.env=="pi"):
                display = auto()

            out = Image.new("RGB", self.dimensions, (255, 255, 255))

            fnt_txt = ImageFont.truetype("assets/arial.ttf", 10)
            fnt_h2 = ImageFont.truetype("assets/arial.ttf", 15)
            d = ImageDraw.Draw(out)

            ##### Tube section
            arrivals = self.tfl.get_arrivals()
            #out.paste(self.tube_logo, (20, 20))

            d.text((self.padding_left, self.padding_top + 60), "Tube Arrivals", font=fnt_h2, fill=(0,0,0))
            d.multiline_text((self.padding_left, self.padding_top + 65), f"{arrivals}", font=fnt_txt, fill=(0, 0, 0))

            ##### News section
            news = self.news.get_news("bbc-news", "")
            d.text((self.padding_left, self.padding_top + 170), "News", font=fnt_h2, fill=(0,0,0))
            d.multiline_text((self.padding_left, self.padding_top + 175), f"{news}", font=fnt_txt, fill=(0, 0, 0))

            news_ai = self.news.get_news("techcrunch", "")
            d.text((self.padding_left, self.padding_top + 230), "Tech news", font=fnt_h2, fill=(0,0,0))
            d.multiline_text((self.padding_left, self.padding_top + 235), f"{news_ai}", font=fnt_txt, fill=(0, 0, 0))

            if(self.env=="pi"):
                display.set_image(out)
            else:
                out.show()
            time.sleep(40)


