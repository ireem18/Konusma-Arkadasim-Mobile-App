from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from uploadapp.views import FileUploadView

urlpatterns = [
    path('', FileUploadView.as_view())

]