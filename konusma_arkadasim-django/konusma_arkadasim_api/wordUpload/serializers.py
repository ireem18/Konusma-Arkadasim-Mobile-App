from rest_framework import serializers

from .models import FileAudioWord


class FileSerializerWord(serializers.ModelSerializer):
    class Meta:
        model = FileAudioWord
        fields = "__all__"
# bu serileştirmek diye türkçeleştirilmiş ama json veriyi yapıp çekmeye yarıyor
# tam olarak işlevi json yapmak sanırım