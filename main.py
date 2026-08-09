from clients.tfl import tflClient
from clients.weather import weatherClient
from clients.spotify import spotifyClient
import os

tfl = tflClient()
weather = weatherClient()
spotify = spotifyClient()

#tfl.get_arrivals()
#weather.get_weather()
#spotify.get_playback()