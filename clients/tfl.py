# TFL Client
import requests, json, os
from dotenv import load_dotenv

load_dotenv()

class tflClient:
    def __init__(self):
        self.station_id = os.environ["STATION_ID"]
        self.arrivals_url = f"https://api.tfl.gov.uk/StopPoint/{self.station_id}/arrivals"

    def get_arrivals(self):
        try:
            resp = requests.get(self.arrivals_url)
            resp.raise_for_status
            status = resp.json()

            for arrival in status:
                time_to_station = int(float(arrival.get("timeToStation")) / 60)
                platform = arrival.get("platformName")
                towards = arrival.get("towards")
                print(f"{towards} at {platform} arriving in {time_to_station} mins")
        except requests.RequestException as e:
            print(f"Error fetching data: {e}")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
