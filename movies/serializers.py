from rest_framework import serializers
from genres.serializers import GenreSerializer
from movies.models import Movie
from genres.models import Genre
from project.exceptions import ValueException

class MovieSerializer(serializers.Serializer):

    id = serializers.UUIDField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10)
    premiere = serializers.DateField()
    classification = serializers.IntegerField()
    synopsis = serializers.CharField()

    genres = GenreSerializer(many=True)

    def create(self, validated_data):

        genres = validated_data.pop("genres")

        movie = Movie.objects.create(**validated_data) 

        for genre in genres:
            genre_already_exists = Genre.objects.filter(name=genre["name"]).values()

            if not genre_already_exists:
                create_new_genre = Genre.objects.create(**genre)
                movie.genres.add(create_new_genre)
            else:
                movie.genres.add(genre_already_exists[0]["id"])

        return movie

    def update(self, instance, validated_data):

        if "genres" in validated_data.keys():
            
            genres = validated_data.pop("genres")

            if len(genres) > 1:
                raise ValueException({"detail":"You can set only one new genre per request"})

            for genre in genres:
                genre_already_exists = Genre.objects.filter(name=genre["name"]).values()

            if genre_already_exists:
                instance.genres.add(genre_already_exists[0]["id"])
            else:
                create_new_genre = Genre.objects.create(**genre)
                instance.genres.add(create_new_genre)
               
        for key, value in validated_data.items():
            setattr(instance,key,value)

            instance.save()

        return instance
