# Spotify Playlist Viewer App

This project is a simple web app built using Flask and the Spotipy library to authenticate users with Spotify, display their playlists, and allow them to log out. The app was created by following the step-by-step tutorial by [Imdad Codes on YouTube](https://www.youtube.com/watch?v=2if5xSaZJlg&t=2147s). I wanted to use this tutorial to get a basic understanding of Spotify API in order to build future data analytic projects. 

# Features

- **Spotify authentication** using OAuth2
- **Display the user's Spotify playlists** with links
- **Logout functionality** to clear the session

# Requirements

This project requires the following libraries to be installed:

- Python 3.x
- Flask
- Spotipy
- python-dotenv

The required dependencies can be found in requirements.txt 

# Setup

## 1. Clone the Repository 

Clone the repository to your local machine:

```
git clone <repository_url>
cd <repository_directory>
```

## 2. Set Up API Credentials

Create a .env file in the root of the project directory with your Spotify API credentials:

```
CLIENT_ID=<your_spotify_client_id>
CLIENT_SECRET=<your_spotify_client_secret>
```

## 3. Run the Application

Start the Flask app by running:

```
python app.py
```

This will start a Flask server locally at http://localhost:5000

## 4. Authentication

When you visit the app, you will be redirected to Spotify for authentication. Once authenticated, you'll be redirected back to the app, where your playlists will be displayed.

# Endpoints

The app provides the following routes:

- '/': The home page. If the user is not authenticated, they are redirected to Spotify's OAuth page.
- '/callback': The redirect URI used by Spotify after successful authentication. It retrieves the access token and redirects to the playlist viewer.
- '/get_playlists': Displays the user's Spotify playlists, including their name and a link to each.
- '/logout': Clears the session and redirects back to the home page.

# Acknowledgments

This project was created by following the tutorial by [Imdad Codes](https://youtu.be/2if5xSaZJlg?si=MgXFve5t973aSoqY).

