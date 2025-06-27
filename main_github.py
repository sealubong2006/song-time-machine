# Import necessary libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd
import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint

# Load environment variables from a .env file
load_dotenv()

# Prompt user for a date and validate the format
while True:
    year_to_travel = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
    try:
        date = pd.to_datetime(year_to_travel, format="%Y-%m-%d")
    except ValueError:
        print("You have entered an invalid date format.. try again")
        continue
    else:
        break

# Set headers to mimic a browser visit (avoids some scraping blocks)
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"
}

# Construct the Billboard URL for the specified date
billboard_url = "https://www.billboard.com/charts/hot-100/" + year_to_travel
response = requests.get(billboard_url, headers=header)
billboard_html_doc = response.text

# Parse HTML using BeautifulSoup
soup = BeautifulSoup(billboard_html_doc, "html.parser")

# Extract song titles from the page
title_of_songs = soup.select("li ul li h3")
song_titles = [song.text.strip() for song in title_of_songs]  # Clean whitespace

# Print the list of song titles
pprint(song_titles)

# Load Spotify credentials from environment variables
CLIENT_ID = os.getenv("CLIENT_ID")  # <-- Put your Spotify Client ID in the .env file
CLIENT_SECRET = os.getenv("CLIENT_SECRET")  # <-- Put your Spotify Client Secret in the .env file
REDIRECT_URL = os.getenv("SPOTIFY_REDIRECT_URL")  # <-- Use a valid redirect URL
SPOTIFY_DISPLAY_NAME = os.getenv("SPOTIFY_DISPLAY_NAME")  # <-- Your Spotify display name
USER_ID = os.getenv("USER_ID")  # <-- Your Spotify user ID

# Authenticate with Spotify using Spotipy
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URL,
        scope="playlist-modify-private",
        show_dialog=True,
        cache_path=".cache",
        username=SPOTIFY_DISPLAY_NAME
    )
)

# Extract the year for searching more accurately in Spotify
year = year_to_travel.split("-")[0]
song_uri = []

# Search each song on Spotify and collect its URI
for song in song_titles:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uri.append(uri)
    except IndexError:
        print(f"{song} does not exist in Spotify.. skipped.")

# Create a new private playlist on Spotify
create_playlist = sp.user_playlist_create(
    user=USER_ID,
    name=f"{year_to_travel} Billboard 100",
    public=False,
    collaborative=False,
    description="Throwback songs to relieve the good days"
)

# Add the found tracks to the new playlist
add_tracks = sp.playlist_add_items(
    playlist_id=create_playlist["id"],
    items=song_uri,
)
