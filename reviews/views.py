from rest_framework.views import APIView, Request, Response, status
from project.exceptions import NotFoundException
from reviews.models import Review
from reviews.serializer import ReviewSerializer

from rest_framework.authentication import TokenAuthentication

from project.pagination import CustomPageNumberPagination

class ReviewView(APIView, CustomPageNumberPagination):
    authentication_classes = [TokenAuthentication]
    def get(self, req: Request):
        reviews = Review.objects.all()

        result_per_page = self.paginate_queryset(reviews, req, view=self)

        serialized = ReviewSerializer(result_per_page, many=True)

        return Response(serialized.data, status.HTTP_200_OK)

class ReviewMovieView(APIView, CustomPageNumberPagination):
    authentication_classes = [TokenAuthentication]

    def get(self, req: Request, movie_id):
        reviews = Review.objects.filter(movie_id=movie_id).first()

        result_page = self.paginate_queryset(reviews, req, view=self)

        serialized = ReviewSerializer(result_page, many=True)
        
        return Response(serialized.data, status.HTTP_200_OK)


    def post(self, req: Request, movie_id):

        if req.user.is_staff:
            serialized = ReviewSerializer(data=req.data)
            serialized.is_valid(raise_exception=True)
            serialized.save(critic=req.user, movie_id=movie_id)

            return Response(serialized.data, status.HTTP_201_CREATED)

        return Response({"detail": "User not authenticated."}, status.HTTP_401_UNAUTHORIZED)

class ReviewViewByID(APIView):
    authentication_classes = [TokenAuthentication]

    def delete(self, req: Request, review_id):
        if req.user.is_staff:
            review = Review.objects.filter(id=review_id).first()
            if not review:
                raise NotFoundException({"detail":"Review not found."})

            serialized = ReviewSerializer(review)
        
            if serialized.data["critic"] != req.user.id and not req.user.is_superuser:
                return Response({"detail": "You can't delete this review."}, status.HTTP_401_UNAUTHORIZED)

            review.delete()

            return Response("", status.HTTP_204_NO_CONTENT)

        return Response({"detail": "User not authenticated."}, status.HTTP_401_UNAUTHORIZED)