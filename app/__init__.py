from flask import Flask
import os
# from flask.ext.login import LoginManager
# from flask.ext.sqlalchemy import SQLAlchemy
from flask_oauthlib.client import OAuth

# configuration
# instance folder (recpotify/instance/) not included in public repo
app = Flask(__name__,instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')

# spotify oauth varaibles
oauth=OAuth(app)
remote_app = oauth.remote_app(
    name = 'spotify',
    content_type = 'application/json',
    request_token_params={'scope': 'user-read-email playlist-read-private playlist-read-collaborative user-follow-read playlist-modify-private'},
    base_url='https://api.spotify.com',
    request_token_url=None,
    access_token_url='https://accounts.spotify.com/api/token',
    authorize_url='https://accounts.spotify.com/authorize',
    app_key = 'SPOTIFY'
    )
from .helper import SpotifyRemoteApp
from config import API_VERSION
spotify = SpotifyRemoteApp(remote_app, API_VERSION)

# setting up cache
from flask.ext.cache import Cache
from config import CACHE_CONFIG
cache = Cache(app, config=CACHE_CONFIG)

log = app.logger

# database variables
# db = SQLAlchemy(app)
# lm = LoginManager()
# lm.init_app(app)
# lm.login_view = 'login'
from app import views
# from app import views, models
