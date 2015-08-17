
# patch OAuthRemoteApp to be more spotify friendly
import types
from flask_oauthlib.client import *


# def spotify_patch(remoteapp):
#     assert isinstance(remoteapp, OAuthRemoteApp)

#     def method(target):
#         print "x=",x
#         print "called from", target
#     target.method = types.MethodType(method,target)

class SpotifyRemoteApp(OAuthRemoteApp):

    def __init__(self, remote_app):
        assert isinstance(remote_app, OAuthRemoteApp)
        remote_dict = remote_app.__dict__
        super().__init__(oauth=remote_dict['oauth'],name = remote_dict['name'],app_key = remote_dict['app_key'])
        self.__dict__ = remote_dict

    def get_user(self):
        return self.get('/v1/me')
