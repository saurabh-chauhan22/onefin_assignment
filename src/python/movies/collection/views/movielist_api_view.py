'''
Movies list api view
'''
import os
import requests

from urllib.parse import urlparse, urlunparse, parse_qs, urlencode

from django.http import JsonResponse

from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from ..serializers import MovieSerializer
from ..token_authenticator import TokenAuthentication


__all__ = ['MovieListApiView']

class MovieListApiView(ListAPIView):
    '''
    Get the list of movies from the api url and display the response
    '''
    authentication_classes = [TokenAuthentication]
    serializer_class = MovieSerializer

    API_URL = 'https://demo.credy.in/api/v1/maya/movies/'

    result_data = None

    def get_queryset(self):
        '''
        return the data from the api url 
        retry count will try to get the response from the api 
        3 times if it does not get reponse
        '''
        data = list()
        retry_count = 0
        
        retry_count = 0
        while retry_count < 3:
            response = requests.get(self.API_URL)
            if response.status_code == 200:
                data = response.json()
                self.result_data = data
                data = data['results']
            retry_count += 1
        return data

    def get_count(self):
        '''
        Return the count of movies data or the page size
        '''
        return self.paginator.page_size if not self.result_data else self.result_data.get('count')
        
    def get_next_url(self):
        '''
        Get the next url for movies data from the api
        parse the url
        '''
        if self.result_data and self.result_data['next']:
            next_url = self.result_data['next']
            # page_number = next_url.split('?page=')[-1]
            url_parts = list(urlparse(self.request.build_absolute_uri()))
            query_params = parse_qs(url_parts[4])
            query_params['page'] = next_url[-1]
            url_parts[4] = urlencode(query_params, doseq=True)
            return urlunparse(url_parts)
        return None
    
    def get_prev_url(self):
        '''
        Get the previous link url for movies data from the api
        '''
        if self.result_data and self.result_data['previous']:
            previous_url = self.result_data['previous']
            # page_number = next_url.split('?page=')[-1]
            url_parts = list(urlparse(self.request.build_absolute_uri()))
            query_params = parse_qs(url_parts[4])
            query_params['page'] = previous_url[-1]
            url_parts[4] = urlencode(query_params, doseq=True)
            return urlunparse(url_parts)
        return None
    
    def get_paginated_response(self, data):
        '''
        Return the paginated response with next url, prev url
        count of movies on the page and movies data
        '''        
        return Response({
            'count': self.get_count(),
            'next': self.get_next_url(),
            'previous': self.get_prev_url(),
            'data': data 
        })


