from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView, ListAPIView, get_object_or_404, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerializer
from .models import LoginUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer



"""
class UserView(APIView):
    def get(self, request):
        users = User.objects.all()
        # the many param informs the serializer that it will be serializing more than a single article.
        serializer = UserSerializer(users, many=True)
        return Response({"users": serializer.data})

    def post(self, request):
        user = request.data.get('user')

        # Create an article from the above data
        serializer = UserSerializer(data=user)
        if serializer.is_valid(raise_exception=True):
            user_saved = serializer.save()
        return Response({"success": "User '{}' created successfully".format(user_saved.username)})


class UserLoginView(CreateAPIView, ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserLoginSerializer
    authentication_classes = (TokenAuthentication,)

    def perform_create(self, serializer):
        user = get_object_or_404(User, id=self.request.data.get('username'))
        return serializer.save(user=user)

class SingleUserView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserLoginSerializer
"""