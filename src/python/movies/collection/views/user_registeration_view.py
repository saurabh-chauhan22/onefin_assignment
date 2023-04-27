from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class RegisterView(APIView):
    '''
    Registeration of new user using default user model and auth
    token 
    '''
    def post(self, request):
        '''
        get the username and password and create user and token for that user
        and return token response
        '''
        username = request.data.get("username", None)
        password = request.data.get("password", None)
        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already exists."}, status=400)
        user = User.objects.create_user(username=username, password=password)
        token = Token.objects.create(user=user)
        return Response({"access_token": token.key})