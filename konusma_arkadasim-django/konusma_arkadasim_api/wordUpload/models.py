from django.db import models

# Create your models here.
from rest_framework.fields import ListField


class FileAudioWord(models.Model):
    file = models.FileField(blank=False, null=False)
    user = models.CharField(max_length=20)

    def __str__(self):
        return self.file.name