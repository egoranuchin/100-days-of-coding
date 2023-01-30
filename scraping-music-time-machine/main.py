from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

URL = "https://www.billboard.com/charts/hot-100/2000-08-12/"

SPOTIFY_CLIENT_ID = "3f398ab60d5b4042ad700df7913b20e4"
SPOTIFY_CLIENT_SECRET = "88cad39968d64dcfb12a7869e808b5a7"
SPOTIFY_REDIRECT_URI = "http://example.com"

### SPOTIFY AUTH

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=SPOTIFY_REDIRECT_URI,
        client_id= SPOTIFY_CLIENT_ID,
        client_secret= SPOTIFY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]

print(user_id)

### GET USER DATE

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")

## GET SONG TITLES

response = requests.get(URL)

soup = BeautifulSoup(response.text, "html.parser")

song_names_h3 = soup.select(".o-chart-results-list__item h3.c-title")
song_names = [song.getText().strip() for song in song_names_h3]

# print(song_names)

### SEARCH FOR SONG TITLES IN SPOTIFY

song_uris = []
year = date.split("-")[0]

for song in song_names:
    result = sp.search(q=f"track: {song}  ", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")


### CREATING A SPOTIFY PLAYLIST

playlist = sp.user_playlist_create(
    user=user_id,
    name=f"{date} Billboard 100",
    public=False
)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)