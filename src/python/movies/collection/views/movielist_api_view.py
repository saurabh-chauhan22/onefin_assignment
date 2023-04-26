'''
Movies list api view
'''
import requests

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

__all__ = ['MovieListApiView']

class MovieListApiView(APIView):
    '''
    Get the list of movies from the api url and display the response
    '''
    API_URL = 'https://demo.credy.in/api/v1/maya/movies/'

    def get(self, request):
        response = requests.get(self.API_URL)
        data = response.json()
        results = data['results']
        return Response(results,status.HTTP_200_OK)
            
