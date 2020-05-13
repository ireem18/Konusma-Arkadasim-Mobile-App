from django.contrib.auth.models import User
from rest_framework import serializers

from .models import LoginUser

class UserSerializer (serializers.HyperlinkedModelSerializer):
    class Meta :
        model = User
        fields =['id','username','email','password']
        extra_kwargs ={'password' : {'write_only':True,'required':True}}
    def create(self,validated_data):
        user = User.objects.create_user(**validated_data)
        return user






"""
class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=120)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=255)

    def create(self, validated_data):
        return User.objects.create(**validated_data)

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=120)
    password = serializers.CharField(max_length=255)

    def create(self, validated_data):
        return User.objects.create(**validated_data)
"""