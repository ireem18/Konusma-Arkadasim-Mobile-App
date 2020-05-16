from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import FileSerializer
from . import wav_split

file_path='C:/Users/Lenovo/Desktop/django-ionic/konusma_arkadasim-django/konusma_arkadasim_api/media/'

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
            seconds = (QueryDict['duraction_time']).split(",")
            seconds = [int(i) for i in seconds]
            print((QueryDict['duraction_time']))
            print((QueryDict['duraction_time']).split(","))
            print(str(QueryDict['user']))
            print(str(QueryDict['file']))
            print(QueryDict)
            wav_split.wav_split(fileName=fileName,seconds=seconds,ad=isim)
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        ##### burada geri yazı gönder .