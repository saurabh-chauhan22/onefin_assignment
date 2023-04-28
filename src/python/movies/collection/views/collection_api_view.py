from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Collection
from ..models import Movie
from ..serializers import CollectionSerializer
from ..token_authenticator import TokenAuthentication

class CollectionView(APIView):
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        '''
        Request all the movies and get the favourite genres of movies and return
        the collection data
        '''
        genres = dict()
        for movie in Collection.objects.get_all_movies(request.user):
            genres[movie.genres] = genres.get(movie.genres, 0) + 1
        sorted_genres = sorted(genres.items(), key=lambda x: x[1], reverse=True)
        top_genres = [genre[0] for genre in sorted_genres[:3]]
        collection_qs = Collection.objects.filter(user=request.user)
        if collection_qs is not None:
            response_data = {
                "collections": [{"title": collection.title, "uuid": str(collection.uuid), "description": collection.description}\
                                for collection in collection_qs],
                "favourite_genres": ", ".join(top_genres)
            }
        return Response({"is_success": True, "data": response_data})
    
    def post(self, request):
        '''
        Create the collection for the user with the movies from 
        the request data and return with collection_uuid response
        '''
        data = request.data
        collection = Collection.objects.create(title=data["title"], description=data["description"], user=request.user)
        for movie_data in data.get("movies", []):
            movie, created = Movie.objects.get_or_create(title=movie_data["title"], uuid=movie_data["uuid"], defaults={"description": movie_data["description"], "genres": movie_data["genres"]})
            movie.save()
            collection.add_movie_to_collection(movie)
        return Response({"collection_uuid": collection.uuid})
    

class CollectionDetailView(APIView):
    '''
    Collection detail view to get the collections data for user 
    or update the data
    '''
    authentication_classes = [TokenAuthentication]

    def get(self, request, collection_uuid):
        '''
        Get the Collection data from uuid and return the response
        '''
        collection = get_object_or_404(Collection, uuid=collection_uuid)
        serializer = CollectionSerializer(collection)
        return Response(serializer.data)
    
    def put(self, request, collection_uuid):
        '''
        Update the data of the collection uuid 
        save and return the response data or return serializer error with
        http 400
        '''
        collection = get_object_or_404(Collection, uuid=collection_uuid)
        serializer = CollectionSerializer(collection, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

