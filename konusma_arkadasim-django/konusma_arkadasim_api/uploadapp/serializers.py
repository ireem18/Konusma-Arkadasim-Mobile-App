from rest_framework import serializers

from .models import FileAudio


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileAudio
        fields = "__all__"

