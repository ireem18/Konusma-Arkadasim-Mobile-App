from django.contrib.auth.models import User
from rest_framework import serializers

from .models import offerWord

class WordSerializer(serializers.ModelSerializer):
    class Meta :
        model = offerWord
        fields =['id','letter','word','image']

