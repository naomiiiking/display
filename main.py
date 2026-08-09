from clients.tfl import tflClient
from clients.weather import weatherClient
from clients.spotify import spotifyClient
from clients.news import newsClient

tfl = tflClient()
weather = weatherClient()
spotify = spotifyClient()
news = newsClient()

#tfl.get_arrivals()
#weather.get_weather()
#spotify.get_playback()
news.get_news("techcrunch", "Tech", "AI")
news.get_news("bbc-news", "", "")
