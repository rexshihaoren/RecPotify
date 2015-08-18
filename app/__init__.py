from flask import Flask
import os
basedir = os.path.abspath(os.path.dirname('__file__'))

# configuration
app = Flask(__name__)
app.config.from_object('config.default')

# Load the file specified by the APP_CONFIG_FILE environment variable
# Variables defined here will override those in the default configuration
CONFIG_FILE_PATH = os.path.join(basedir, os.environ.get('APP_CONFIG_FILE'))
app.config.from_pyfile(CONFIG_FILE_PATH)

# spotify oauth varaibles
from flask_oauthlib.client import OAuth
oauth=OAuth(app)
remote_app = oauth.remote_app(
    name = 'spotify',
    content_type = 'application/json',
    request_token_params={'scope': 'user-read-email playlist-read-private playlist-read-collaborative user-follow-read playlist-modify-private'},
    base_url='https://api.spotify.com',
    request_token_url=None,
    access_token_url='https://accounts.spotify.com/api/token',
    authorize_url='https://accounts.spotify.com/authorize',
    app_key= 'SPOTIFY'
    )

from .helper import SpotifyRemoteApp
spotify = SpotifyRemoteApp(remote_app, app.config['API_VERSION'])

# setting up cache
from flask.ext.cache import Cache
cache = Cache(app, config=app.config['CACHE_CONFIG'])

# logging set up
log = app.logger

# from flask.ext.login import LoginManager
# from flask.ext.sqlalchemy import SQLAlchemy
# database variables
# db = SQLAlchemy(app)
# lm = LoginManager()
# lm.init_app(app)
# lm.login_view = 'login'
from app import views
# from app import views, models
