
from social_core.backends.facebook import FacebookOAuth2

"""
Facebook OAuth2 and Canvas Application backends, docs at:
    https://python-social-auth.readthedocs.io/en/latest/backends/facebook.html
"""

from social_core.utils import handle_http_errors
from social_core.exceptions import AuthUnknownError, \
    AuthMissingParameter

# API_VERSION = 2.9

class FacebookOAuth2Token(FacebookOAuth2):
    """Facebook OAuth2 authentication backend"""

    name = 'facebook-token'

    @handle_http_errors
    def auth_complete(self, *args, **kwargs):
        """Completes loging process, must return user instance"""
        self.process_error(self.data)
        if not self.data.get('access_token'):
            raise AuthMissingParameter(self, 'access_token')
        # API v2.3 returns a JSON, according to the documents linked at issue
        # #592, but it seems that this needs to be enabled(?), otherwise the
        # usual querystring type response is returned.

        return self.do_auth(self.data['access_token'], *args, **kwargs)

    def do_auth(self, access_token, response=None, *args, **kwargs):
        # response = response or {}

        data = self.user_data(access_token)

        if not isinstance(data, dict):
            # From time to time Facebook responds back a JSON with just
            # False as value, the reason is still unknown, but since the
            # data is needed (it contains the user ID used to identify the
            # account on further logins), this app cannot allow it to
            # continue with the auth process.
            raise AuthUnknownError(self, 'An error ocurred while retrieving '
                                         'users Facebook data')

        data['access_token'] = access_token
        # if 'expires_in' in response:
        #     data['expires'] = response['expires_in']
        #
        # if self.data.get('granted_scopes'):
        #     data['granted_scopes'] = self.data['granted_scopes'].split(',')
        #
        # if self.data.get('denied_scopes'):
        #     data['denied_scopes'] = self.data['denied_scopes'].split(',')

        kwargs.update({'backend': self, 'response': data})
        return self.strategy.authenticate(*args, **kwargs)
