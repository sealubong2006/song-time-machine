# 🎵 Billboard to Spotify Playlist Generator

This project takes the Billboard Hot 100 songs from any date in the past or present and creates a private Spotify playlist from it — automatically!

## 🌟 What It Does

You pick a date (like `2010-06-25`) and this script:

1. Scrapes the Billboard Hot 100 songs from that day.
2. Searches for those songs on Spotify.
3. Creates a private playlist in your Spotify account with those songs.

## 🚀 Getting Started

### Prerequisites

* Python 3 installed
* A Spotify developer account ([https://developer.spotify.com/dashboard/](https://developer.spotify.com/dashboard/))
* Spotify account
* Pip installed (`pip --version`)

### 1. Clone This Project

```bash
git clone https://github.com/yourusername/billboard-spotify-playlist.git
cd billboard-spotify-playlist
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Create a `.env` File

Create a `.env` file in the project root directory with the following variables:

```
CLIENT_ID=your_spotify_client_id
CLIENT_SECRET=your_spotify_client_secret
SPOTIFY_REDIRECT_URL=http://localhost:8888/callback
SPOTIFY_DISPLAY_NAME=your_spotify_display_name
USER_ID=your_spotify_user_id
```

> 🔐 **Note:** Never share this file or commit it to GitHub! Add `.env` to your `.gitignore`.

### 4. Run the Script

```bash
python your_script_name.py
```

When prompted, enter a date like `1999-12-25`.

A browser window will open asking you to authorize access to your Spotify account. Click **Agree**.

If successful, a new private playlist will be created in your Spotify account!

## ❗ Notes

* Not all Billboard songs may exist on Spotify. The script will skip any missing ones.
* You need to allow the scope `playlist-modify-private` in your Spotify app settings.
* Make sure your redirect URI in the Spotify developer dashboard matches the one in your `.env`.

## 🛠 Tech Stack

* Python
* BeautifulSoup (for web scraping)
* Spotipy (Spotify API wrapper)
* pandas & dotenv


📜 Disclaimer
This project is for educational and personal learning purposes only.

The song data used in this project is sourced from the publicly accessible [Billboard Hot 100 page]("https://www.billboard.com/charts/hot-100/"). I do not claim ownership of any Billboard content, nor am I affiliated with Billboard or Spotify.

This script is intended to help developers learn web scraping, APIs, and automation using Python.

If Billboard or Spotify requests this project be taken down, I will comply immediately.
