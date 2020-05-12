from django.contrib import admin

from LoginUser.models import LoginUser, UserInfo

admin.site.register(LoginUser)
admin.site.register(UserInfo)