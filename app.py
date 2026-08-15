from clients.tfl import tflClient
from clients.weather import weatherClient
from clients.spotify import spotifyClient
from clients.news import newsClient
from PIL import Image, ImageDraw, ImageFont


class App:
    def __init__(self):
        self.tfl = tflClient()
        self.weather = weatherClient()
        self.spotify = spotifyClient()
        self.news = newsClient()
        self.dimensions = (400, 300) # 4.2 Inky wHAT
        self.padding_top = 5
        self.padding_left = 10

    def run(self):
        #tfl.get_arrivals()
        #weather.get_weather()
        #spotify.get_playback()

        #self.news.get_news("techcrunch", "Tech", "AI")
        #self.news.get_news("bbc-news", "", "")
        out = Image.new("RGB", self.dimensions, (255, 255, 255))

        fnt_txt = ImageFont.truetype("assets/arial.ttf", 10)
        fnt_h2 = ImageFont.truetype("assets/arial.ttf", 15)
        d = ImageDraw.Draw(out)

        ##### Tube section
        

        ##### News section
        news = self.news.get_news("bbc-news", "")
        d.text((self.padding_left, self.padding_top + 170), "News", font=fnt_h2, fill=(0,0,0))
        d.multiline_text((self.padding_left, self.padding_top + 175), f"{news}", font=fnt_txt, fill=(0, 0, 0))

        news_ai = self.news.get_news("techcrunch", "")
        d.text((self.padding_left, self.padding_top + 230), "Tech news", font=fnt_h2, fill=(0,0,0))
        d.multiline_text((self.padding_left, self.padding_top + 235), f"{news_ai}", font=fnt_txt, fill=(0, 0, 0))

        out.show()
