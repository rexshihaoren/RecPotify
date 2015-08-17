
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
        '''Get current user Profile.'''
        return self.get('/me').data

    def get_followed_artists(self):
        '''Get current user followed artists'''
        return self.get('/me/following?type=artist').data

    def get_list_of_playlist(self, user_id):
        '''Get a list of a user's playlists'''
        return self.get('/users/%s/playlists'%user_id).data

    def get_playlist_tracks(self, user_id, playlist_id):
        '''Get the tracks of a user's playlists'''
        return self.get('/users/%s/playlists/%s/tracks'%(user_id,playlist_id)).data
