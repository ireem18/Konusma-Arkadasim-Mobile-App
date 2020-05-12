
from django.db import models

# Create your models here.


class User(models.Model):
    fullName = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    confirmPassword = models.CharField(max_length=20)

    def __str__(self):
        return self.fullName

class Offer(models.Model):
    word = models.CharField(max_length=10)
    image = models.ImageField(upload_to='images/')
    file_audio = models.FileField(upload_to='musics/')
    file_word_audio = models.FileField(upload_to='musics/')
    user_name = models.ForeignKey('User', related_name='offers',on_delete=models.CASCADE)

    def __str__(self):
        return self.word

class AudioRecord(models.Model):
    file_audio = models.FileField(upload_to='musics/')
    user_name = models.ForeignKey('Offer', related_name='audios',on_delete=models.CASCADE)
    def __str__(self):
        return self.user_name

class WordAudioRecord(models.Model):
    file_word_audio = models.FileField(upload_to='musics/')
    user_name = models.ForeignKey('Offer', related_name='words',on_delete=models.CASCADE)
    def __str__(self):
        return self.user_name