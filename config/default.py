import os
basedir = os.path.abspath(os.path.dirname('__file__'))

# spotify oauth configs
API_VERSION = 'v1'
SPOTIFY = {
    'consumer_key':'',
    'consumer_secret':''
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
