
from django.db import models

class LoginUser(models.Model):
  name = models.CharField(max_length=255)
  email = models.EmailField()
  password = models.CharField(max_length=255)
  def __str__(self):
        return self.name

class UserInfo(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    body = models.TextField()
    author = models.ForeignKey('LoginUser', related_name='users', on_delete=models.CASCADE)

    def __str__(self):
        return self.title