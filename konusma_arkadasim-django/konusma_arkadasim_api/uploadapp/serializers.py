from rest_framework import serializers

from .models import FileAudio


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileAudio
        fields = "__all__"
# bu serileştirmek diye türkçeleştirilmiş ama json veriyi yapıp çekmeye yarıyor
# tam olarak işlevi json yapmak sanırım