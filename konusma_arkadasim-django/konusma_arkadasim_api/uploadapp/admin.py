from django.contrib import admin

# Register your models here.
from .models import FileAudio

class FileAdmin(admin.ModelAdmin):
    list_display = ['user','file']

admin.site.register(FileAudio,FileAdmin)