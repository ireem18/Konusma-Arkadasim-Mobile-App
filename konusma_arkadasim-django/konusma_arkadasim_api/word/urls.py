from django.urls import path, include

from .views import WordView

app_name = "words"
urlpatterns = [
    path('words/', WordView.as_view()),
    ]