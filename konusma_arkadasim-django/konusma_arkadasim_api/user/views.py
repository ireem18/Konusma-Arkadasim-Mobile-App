from django.shortcuts import get_object_or_404

# Create your views here.
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView

from user.models import Offer, AudioRecord, User
from .serializers import UserSerializer

"""
class UserView(ListModelMixin,GenericAPIView):
    queryset = Offer.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        user = get_object_or_404(User, id=self.request.data.get('fullName'))
        return serializer.save(author = user)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, *kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)



"""


class UserView(APIView):
    def get(self, request, *args, **kwargs):
        offers = Offer.objects.all()
        serializer = UserSerializer(offers, many=True)
        return Response({'users': serializer.data})

    def post(self, request, *args, **kwargs):
        offer = request.data.get('user')

        serializer = UserSerializer(data=offer)
        if serializer.is_valid(raise_exception=True):
            offer_saved = serializer.save()
        return Response({"success": "Offer '{}' created successfully".format(offer_saved.title)})

    def put(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        saved_offer = get_object_or_404(Offer.objects.all(), pk=pk)
        data = request.data.get('article')
        serializer = UserSerializer(instance=saved_offer, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            offer_saved = serializer.save()
        return Response({"success": "Offer '{}' updated successfully".format(offer_saved.title)})

    def delete(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        offer = get_object_or_404(Offer.objects.all(), pk=pk)
        offer.delete()
        return Response({"message": "Offer with id '{}' has been deleted".format(pk)}, status=204)
