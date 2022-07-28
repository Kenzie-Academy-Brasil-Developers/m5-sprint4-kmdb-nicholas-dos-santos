from django.urls import path
from movies.views import MovieView, MovieIdView

urlpatterns=[
    path("", MovieView.as_view()),
    path("<uuid:movie_id>/", MovieIdView.as_view()),
]