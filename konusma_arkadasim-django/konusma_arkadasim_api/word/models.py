from django.contrib.auth.models import User
from django.db import models
from django.db.models import Model


class offerWord(models.Model):
    LETTER = [
        ('a','a'),
        ('e','e'),
        ('ı','ı'),
        ('i','i'),
        ('u','u'),
        ('ü','ü'),
        ('o','o'),
        ('ö','ö'),
    ]
    letter = models.CharField(choices=LETTER,max_length=1)
    word = models.CharField(max_length=10)
    image = models.ImageField(upload_to='images/')
    listenAudioFile = models.FileField(null=False)

