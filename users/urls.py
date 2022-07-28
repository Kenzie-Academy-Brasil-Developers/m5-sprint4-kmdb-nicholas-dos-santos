from django.urls import path

from users.views import LoginView, UserIdView, UserView, CreateUser

urlpatterns =[
    path("register/", CreateUser.as_view()),
    path("login/", LoginView.as_view()),
    path("", UserView.as_view()),
    path("<uuid:user_id>/", UserIdView.as_view()),
]