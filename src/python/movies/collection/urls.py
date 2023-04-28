'''
Collections api urls.py
'''
from django.urls import path

from .views import MovieListApiView, RequestCounterView, RegisterView, CollectionView, CollectionDetailView

urlpatterns = [
    path('movies/',MovieListApiView.as_view()),
    path('request-count/',RequestCounterView.as_view()),
    path('register/',RegisterView.as_view()),
    path('collection/',CollectionView.as_view()),
    path('collection/<collection_uuid>/',CollectionDetailView.as_view()),

]
