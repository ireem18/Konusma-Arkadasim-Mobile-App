from django.contrib import admin

from .models import LoginUser, UserInfo

admin.site.register(LoginUser)
admin.site.register(UserInfo)