from django.urls import path

from LoginUser.views import  UserView
from rest_framework.authtoken.views import ObtainAuthToken

app_name = "articles"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('users/', UserView.as_view()),
    path('auth/', ObtainAuthToken.as_view())
]