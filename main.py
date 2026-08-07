from clients.tfl import tflClient

tfl = tflClient()

print(tfl.station_id)

tfl.get_arrivals()