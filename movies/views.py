from rest_framework.views import APIView, Request, Response, status
from rest_framework.authentication import TokenAuthentication

from project.exceptions import NotFoundException

from movies.models import Movie
from movies.serializers import MovieSerializer
from movies.permissions import MoviePermission

from project.pagination import CustomPageNumberPagination

import uuid


class MovieView(APIView, CustomPageNumberPagination):
    authentication_classes = [TokenAuthentication]
    permission_classes = [MoviePermission]
    
    def post(self, req: Request):
        serialized = MovieSerializer(data=req.data)

        try:
            serialized.is_valid(raise_exception=True)
            serialized.save()

            return Response(serialized.data, status.HTTP_201_CREATED)

        except ValueError as err:
            return Response(*err.args)

    
    def get(self, req:Request):
        
        movies = Movie.objects.all()

        result_per_page = self.paginate_queryset(movies, req, view=self)

        serialized = MovieSerializer(result_per_page, many=True)

        return Response(serialized.data, status.HTTP_200_OK)
    


class MovieIdView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [MoviePermission]

    def get(self, _:Request,movie_id:uuid):
        
        movie = Movie.objects.filter(id=movie_id).first()

        if not movie:
            raise NotFoundException({"detail":"user not found"})

        serialized = MovieSerializer(movie)

        return Response(serialized.data, status.HTTP_200_OK)


    def patch(self, req:Request,movie_id:uuid):
        try:
            movie = Movie.objects.filter(id=movie_id).first()

            serialized = MovieSerializer(movie, data=req.data, partial=True)
            serialized.is_valid(raise_exception=True)
            serialized.save()

            return Response(serialized.data, status.HTTP_200_OK)

        except KeyError as err:
            return Response(err.args, status.HTTP_400_BAD_REQUEST)

    def delete(self, _:Request,movie_id:uuid):
        movie = Movie.objects.filter(id=movie_id).first()
        movie.delete()

        return Response("", status.HTTP_204_NO_CONTENT)
