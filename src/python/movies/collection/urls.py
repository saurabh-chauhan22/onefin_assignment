'''
Collections api urls.py
'''
from django.urls import path

from .views import MovieListApiView, RequestCounterView, RegisterView

urlpatterns = [
    path('movies/',MovieListApiView.as_view(),name='movies'),
    path('request-count/',RequestCounterView.as_view()),
    path('register/',RegisterView.as_view())
]
