from rest_framework import serializers
from project.exceptions import UniqueException

from users.models import User

class UserSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)

    email = serializers.EmailField()
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    password = serializers.CharField(write_only=True)

    date_joined = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def validate_email(self, email:str):
        email_exists = User.objects.filter(email=email).exists()

        if email_exists:
            raise UniqueException({'detail':['email already exists.']})

        return email


    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(source="username")
    password = serializers.CharField()