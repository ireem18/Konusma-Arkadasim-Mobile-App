from django.contrib import admin
from .models import offerWord

class WordAdmin(admin.ModelAdmin):
    list_display = ['word','letter']

admin.site.register(offerWord, WordAdmin)
