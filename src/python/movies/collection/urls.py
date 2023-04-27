'''
Collections api urls.py
'''
from django.urls import path

from .views import MovieListApiView

urlpatterns = [
    path('movies/',MovieListApiView.as_view(),name='movies')
]