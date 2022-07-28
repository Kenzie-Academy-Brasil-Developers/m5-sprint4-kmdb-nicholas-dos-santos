from rest_framework import serializers
from genres.models import Genre

class GenreSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    name = serializers.CharField(max_length=127)

    def create_genre(self, validate_data):
        genre = Genre.objects.create(**validate_data)
        return genre
        