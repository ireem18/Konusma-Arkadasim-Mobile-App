from django.shortcuts import render, get_object_or_404

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import offerWord
from .serializers import WordSerializer
class WordView(APIView):
    def get(self, request, *args, **kwargs):
        offers = offerWord.objects.all()
        serializer = WordSerializer(offers, many=True)
        return Response({'words': serializer.data})

    def post(self, request, *args, **kwargs):
        offer = request.data.get('username')

        serializer = WordSerializer(data=offer)
        if serializer.is_valid(raise_exception=True):
            offer_saved = serializer.save()
        return Response({"success": "Offer '{}' created successfully".format(offer_saved.title)})

    def put(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        saved_offer = get_object_or_404(offerWord.objects.all(), pk=pk)
        data = request.data.get('word')
        serializer = WordSerializer(instance=saved_offer, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            offer_saved = serializer.save()
        return Response({"success": "Offer '{}' updated successfully".format(offer_saved.title)})

    def delete(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        offer = get_object_or_404(offerWord.objects.all(), pk=pk)
        offer.delete()
        return Response({"message": "Offer with id '{}' has been deleted".format(pk)}, status=204)
