from clients.tfl import tflClient
from clients.weather import weatherClient
import os

tfl = tflClient()
weather = weatherClient()


tfl.get_arrivals()
weather.get_weather()