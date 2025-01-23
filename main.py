import os
from dotenv import load_dotenv
load_dotenv

from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
from spotipy.cache_handler import FlaskSessionCacheHandler
from flask import Flask, session, url_for, request, redirect
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(64)

##SETTING UP AUTHENTICATION

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
REDIRECT_URI = 'http://localhost:5000/callback'
SCOPE = 'playlist-read-private'
CACHE_HANDLER = FlaskSessionCacheHandler(session)

sp_oauth = SpotifyOAuth(
    client_id = CLIENT_ID,
    client_secret = CLIENT_SECRET,
    redirect_uri = REDIRECT_URI,
    scope = SCOPE,
    cache_handler = CACHE_HANDLER,
    show_dialog=True
)

##CREATE INSTANCE OF SPOTIFY CLIENT
sp = Spotify(auth_manager=sp_oauth)

##ENDPOINTS

@app.route('/')
def home():
    if not sp_oauth.validate_token(CACHE_HANDLER.get_cached_token()):
        auth_url = sp_oauth.get_authorize_url()
        return redirect(auth_url)
    return redirect(url_for('get_playlists'))

@app.route('/callback')
def callback():
    sp_oauth.get_access_token(request.args['code'])
    return redirect(url_for('get_playlists'))

@app.route('/get_playlists')
def get_playlists():
    if not sp_oauth.validate_token(CACHE_HANDLER.get_cached_token()):
        auth_url = sp_oauth.get_authorize_url()
        return redirect(auth_url)
    
    playlists = sp.current_user_playlists()
    playlists_info = [(pl['name'], pl['external_urls']['spotify']) for pl in playlists['items']]
    playlists_html = '<br>'.join([f'{name}: {url}' for name, url in playlists_info])
    return playlists_html

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

if __name__=='__main__':
    app.run(debug=True)