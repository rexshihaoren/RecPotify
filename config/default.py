import os
basedir = os.path.abspath(os.path.dirname('__file__'))

# spotify oauth configs
API_VERSION = 'v1'
# need set env vriable SPOTIFY_KEY, SPOTIFY_SECRET
SPOTIFY={'consumer_key': os.environ.get('SPOTIFY_KEY', ''), 'consumer_secret': os.environ.get('SPOTIFY_SECRET', '')
}

# cache configs
CACHE_CONFIG = {'CACHE_TYPE': 'simple'}
PORT = 5000

DEBUG = False
TESTING = False
# CSRF_ENABLED = True
SECRET_KEY = 'recpotify rex'
# # database variables
# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
# SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
