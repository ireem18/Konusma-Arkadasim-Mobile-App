from django.contrib import admin

# Register your models here.
from user.models import User, WordAudioRecord, AudioRecord, Offer

admin.site.register(User)
admin.site.register(Offer)
admin.site.register(AudioRecord)
admin.site.register(WordAudioRecord)
