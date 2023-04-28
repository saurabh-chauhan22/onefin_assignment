from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.models import User

class TokenAuthentication(BaseAuthentication):
    '''
    Token authentication to validate request headers
    with token and check if user has the token  
    '''
    prefix_key = 'Bearer'

    def authenticate(self, request):
        '''
        Get the auth headers and validate the headers with the token 
        prefix key and user token and return user
        '''
        auth_header = request.headers.get('Authorization', None)
        if not auth_header:
            return None
        auth_header = auth_header.split()
        if len(auth_header) != 2:
            raise AuthenticationFailed('Invalid token header')
        prefix = auth_header[0]
        token = auth_header[1]

        if prefix != self.prefix_key:
            raise AuthenticationFailed('Invalid token prefix')

        try:
            user = User.objects.get(auth_token=token)
        except User.DoesNotExist:
            raise AuthenticationFailed('Invalid token')
        
        return (user, None)

    def authenticate_header(self, request):
        '''
        Return the header prefix 
        '''
        return self.prefix_key
