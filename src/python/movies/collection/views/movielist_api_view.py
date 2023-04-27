'''
Movies list api view
'''
import os
import requests

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from ..serializers import MovieSerializer

__all__ = ['MovieListApiView']

class MovieListApiView(APIView):
    '''
    Get the list of movies from the api url and display the response
    '''
    API_URL = 'https://demo.credy.in/api/v1/maya/movies/'

    def get(self, request):
        headers = {
            "Authorization": f"Basic {os.environ.get('movies_api_password',None)}"
        }
        params = {
            "page": 1
        }
        retry_count = 0
        while retry_count < 3:
            response = requests.get(self.API_URL, headers=headers, params=params)
            if response.status_code == 200:
                data = response.json()
                movies = data["results"]
                serializer = MovieSerializer(movies, many=True)
                return Response(serializer.data)
            retry_count += 1
        return Response("Error: Could not retrieve movie data.")
            
