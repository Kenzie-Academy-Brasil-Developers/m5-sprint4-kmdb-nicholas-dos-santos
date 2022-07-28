from rest_framework import serializers

from project.exceptions import NotFoundException, ValueException

from reviews.models import Review
from movies.models import Movie


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = "__all__"
        extra_kwargs = {
            "movie": {
                "required": False
            },
            "critic": {
                "required": False 
            }
        }

    def validate_stars(self, stars):
        if(stars > 10):
            raise serializers.ValidationError(["Ensure this value is less than or equal to 10."])
        elif(stars < 1):
            raise serializers.ValidationError(["Ensure this value is greater than or equal to 1."])

        return stars

    def create(self, validated_data):
        critic = validated_data.pop("critic")
        movie_id = validated_data.pop("movie_id")

        movie = Movie.objects.filter(id=movie_id).first()

        if not movie:
            raise NotFoundException({"detail":"Movie not found."})

        review = Review.objects.create(critic=critic, movie=movie, **validated_data)

        return review