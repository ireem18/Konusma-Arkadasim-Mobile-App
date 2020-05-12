from rest_framework.generics import CreateAPIView, ListAPIView, get_object_or_404, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from LoginUser.models import LoginUser
from LoginUser.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
"""
class UserView(APIView):
    def get(self, request):
        users = LoginUser.objects.all()
        # the many param informs the serializer that it will be serializing more than a single article.
        serializer = UserSerializer(users, many=True)
        return Response({"users": serializer.data})

    def post(self, request):
        user = request.data.get('user')

        # Create an article from the above data
        serializer = UserSerializer(data=user)
        if serializer.is_valid(raise_exception=True):
            user_saved = serializer.save()
        return Response({"success": "User '{}' created successfully".format(user_saved.name)})
    
    """

class UserView(CreateAPIView, ListAPIView):
    queryset = LoginUser.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        user = get_object_or_404(LoginUser, id=self.request.data.get('username'))
        return serializer.save(user=user)

class SingleUserView(RetrieveAPIView):
    queryset = LoginUser.objects.all()
    serializer_class = UserSerializer
