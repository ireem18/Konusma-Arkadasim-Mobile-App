from django.urls import path, include

from .views import UserView

app_name = "offers"
urlpatterns = [
    path('users/', UserView.as_view()),
    ]