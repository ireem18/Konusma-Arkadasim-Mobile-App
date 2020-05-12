from rest_framework import serializers

from LoginUser.models import LoginUser


class UserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=120)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=255)

    def create(self, validated_data):
        return LoginUser.objects.create(**validated_data)