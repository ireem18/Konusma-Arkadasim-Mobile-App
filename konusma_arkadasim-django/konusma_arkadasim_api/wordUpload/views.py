from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import FileSerializerWord
from . import testing_word
from . import hmm_train_word

file_path='C:/Users/Lenovo/Desktop/django-ionic/konusma_arkadasim-django/konusma_arkadasim_api/media/'

class FileUploadWordView(APIView):  # Api görünümü vermek için kullanıyoruz bu kısmı
    parser_class = (FileUploadParser,)
    def post(self, request, *args, **kwargs):
        file_serializer2 = FileSerializerWord(data=request.data)
        if file_serializer2.is_valid():
            file_serializer2.save()
            QueryDict = request.data
            print(QueryDict)
            fileName = str(file_path) + str(QueryDict['file'])
            print(str(QueryDict['user']))
            print(str(QueryDict['file']))
            print(QueryDict)
            print(fileName)
            file =str(QueryDict['file'])
            #hmm_train_word.main()
            sonuc = testing_word.testing(fileName=fileName,file=file)

            return Response(sonuc, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer2.errors, status=status.HTTP_400_BAD_REQUEST)
        ##### burada geri yazı gönder .

