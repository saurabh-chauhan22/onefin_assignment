from rest_framework import serializers

__all__ = ['MovieSerializer']

class MovieSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    genres = serializers.CharField()
    uuid = serializers.UUIDField()