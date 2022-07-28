from django.contrib.auth import authenticate
from rest_framework.views import APIView, Response, Request, status 
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from project.exceptions import NotFoundException

from users.models import User
from users.serializers import UserSerializer, LoginSerializer
from users.permissions import UserPermission

from project.pagination import CustomPageNumberPagination

import uuid

class UserView(APIView, CustomPageNumberPagination):
    authentication_classes = [TokenAuthentication]
    permission_classes = [UserPermission]

    def get(self, req:Request):
        
        users = User.objects.all()

        result_per_page = self.paginate_queryset(users, req, view=self)

        serialized = UserSerializer(result_per_page, many=True)

        return Response(serialized.data, status.HTTP_200_OK)

class UserIdView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [UserPermission]

    def get(self, _:Request, user_id:uuid):

        user = User.objects.filter(id=user_id).first()
        serialized = UserSerializer(user)

        if not user:
            raise NotFoundException({"detail":"user not found"})

        return Response(serialized.data, status.HTTP_200_OK)
        

class CreateUser(APIView):
    def post(self, req: Request):
        serialized = UserSerializer(data=req.data)

        try:
            serialized.is_valid(raise_exception=True)
            serialized.save()

            return Response(serialized.data, status.HTTP_201_CREATED)

        except ValueError as err:
            return Response(*err.args)

class LoginView(APIView):
    def post(self, req: Request):
        serialized = LoginSerializer(data=req.data)
        serialized.is_valid(raise_exception=True)

        user: User = authenticate(**serialized.validated_data)

        if not user:
            return Response(
                {"detail": "Invalid credentials"}, status.HTTP_401_UNAUTHORIZED
            )

        token,_ = Token.objects.get_or_create(user=user)

        return Response({"token":token.key}, status.HTTP_200_OK)

