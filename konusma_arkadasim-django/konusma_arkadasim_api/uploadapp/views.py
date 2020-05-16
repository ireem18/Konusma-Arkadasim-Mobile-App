from django.shortcuts import render

# Create your views here.
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import FileAudio
from .serializers import FileSerializer

import librosa
from pydub import AudioSegment


file_path='C:/Users/Lenovo/Desktop/django-ionic/konusma_arkadasim-django/konusma_arkadasim_api/media/'
def wav_split(fileName, seconds, ad):
    readWav = AudioSegment.from_wav(fileName)
    for i in seconds:
        t1 = (i - 1) * 500
        t2 = (i + 1) * 500
        print("t1 : ", t1)
        print("t2 : ", t2)
        newWav = readWav[t1:t2]
        file = fileName
        newWav.export(str(file_path)+'split_audio/' + ad + '-' + str(i) + '.wav', format='wav')
    y, sr = librosa.load(fileName)
    split_interval = librosa.effects.split(y, top_db=1000, hop_length=10000)
    print(split_interval)


class FileUploadView(APIView):  # Api görünümü vermek için kullanıyoruz bu kısmı
    parser_class = (FileUploadParser,)
    def post(self, request, *args, **kwargs):
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            QueryDict = request.data
            print(QueryDict)
            fileName = str(file_path) + str(QueryDict['file'])
            isim = str(QueryDict['user'])
            seconds = [int(QueryDict['duraction_time'])]
            print([int(QueryDict['duraction_time'])])
            print(str(QueryDict['user']))
            print(str(QueryDict['file']))
            wav_split(fileName=fileName, seconds=seconds, ad=isim)
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        ##### burada geri yazı gönder .