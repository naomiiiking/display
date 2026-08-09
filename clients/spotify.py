import spotipy, json
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

load_dotenv()

class spotifyClient():
    def __init__(self):
        self.scope = "user-read-playback-state"
        self.auth_manger = SpotifyClientCredentials()
        self.sp = spotipy.Spotify(auth_manager=self.auth_manger)

    def get_playback(self):
        try:
            results = self.sp.current_playback()
            if results:
                item = (results.get("item")).get("album")

                artists_list = item.get("artists")
                artists = [artist.get("name") for artist in artists_list]
                artists = ", ".join(artists)

                images = item.get("images")
                image = images[2]
                image_url = image.get("url")

                track = item.get("name")

                ouput = f"""
                Currently listening to {track}
                By {artists}
                """

                print(ouput)

            else:
                print("No current Spotify playback")
        except spotipy.exceptions.SpotifyException as e:
            print(f"Error fetching current playback: {e}")