from rest_framework import serializers

from ..models import Collection, Movie
from .movie_serializer import MovieSerializer

class CollectionSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True)

    class Meta:
        model = Collection
        fields = ('title', 'description', 'movies')

    def update(self, instance, validated_data):

        movie_data = validated_data.get('movies')
        if movie_data:
            for movie in movie_data:
                instance.movies.add(Movie.objects.get_or_create(movie_data))

        return instance
