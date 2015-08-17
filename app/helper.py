
# SpotifyRemoteApp is a spotify-friendlier version of OAuthRemoteApp
from flask_oauthlib.client import *
# This might be useful in the future when I want to turn any function into lazy property
from werkzeug import cached_property
class SpotifyRemoteApp(OAuthRemoteApp):

    def __init__(self, remote_app, api_version = 'v1'):
        assert isinstance(remote_app, OAuthRemoteApp)
        remote_dict = remote_app.__dict__
        super().__init__(oauth=remote_dict['oauth'],name = remote_dict['name'],app_key = remote_dict['app_key'])
        self.__dict__ = remote_dict
        self.api_version = api_version


    def request(self, url, *args, **kwargs):
        url= '/'+self.api_version + url
        return super().request(url, *args, **kwargs)


    def get_user(self):
        return self.get('/me')

    def get_followed_artists(self):
        return self.get('/me/following?type=artist')
