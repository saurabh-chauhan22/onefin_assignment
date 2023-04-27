from rest_framework import serializers

__all__ = ['MovieSerializer']

class MovieSerializer(serializers.Serializer):
    title = serializers.CharField()
    genre = serializers.CharField()
    release_year = serializers.IntegerField()