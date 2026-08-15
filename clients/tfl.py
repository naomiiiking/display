# TFL Client
import requests, json, os
from dotenv import load_dotenv

load_dotenv()

class tflClient:
    def __init__(self):
        self.station_id = os.environ["STATION_ID"]
        self.arrivals_url = f"https://api.tfl.gov.uk/StopPoint/{self.station_id}/arrivals"
        self.target_platform = os.environ["TARGET_PLATFORM"]
        self.station_distance = os.environ["WALKING_DISTANCE"]

    def sortTuple(self, e):
        return e[1]
    
    def get_arrivals(self):
        try:
            resp = requests.get(self.arrivals_url)
            resp.raise_for_status
            status = resp.json()
            output = []
            for arrival in status:
                platform = arrival.get("platformName")
                if(platform == self.target_platform):
                    time_to_station = int(float(arrival.get("timeToStation")) / 60)
                    towards = arrival.get("towards")
                    output.append((towards, time_to_station))
            output.sort(key=self.sortTuple)

            outputStr = ""
            for o in output:
                outputStr += f"\n{o[0]} in {o[1]} mins"

            return outputStr
        except requests.RequestException as e:
            print(f"Error fetching tube data: {e}")
        except json.JSONDecodeError as e:
            print(f"Error decoding tube JSON: {e}")
