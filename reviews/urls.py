from django.urls import path
from reviews.views import ReviewMovieView, ReviewViewByID, ReviewView


urlpatterns = [
    path("movies/<uuid:movie_id>/reviews/", ReviewMovieView.as_view()),
    path("reviews/<uuid:review_id>/", ReviewViewByID.as_view()),
    path("reviews/", ReviewView.as_view())
]