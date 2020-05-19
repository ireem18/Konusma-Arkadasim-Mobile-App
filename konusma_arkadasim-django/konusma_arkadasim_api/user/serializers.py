from rest_framework import serializers

from .models import Offer, User


class UserSerializer ( serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ('user_name','word','image','file_audio','file_word_audio')
"""
class UserSerializer(serializers.Serializer):
    user_name = serializers.CharField()
    word = serializers.CharField(max_length=120)
    image = serializers.FileField()
    #file_audio = serializers.FileField()
    #file_word_audio = serializers.FileField()
    def create(self, validated_data):
        return Offer.objects.create(**validated_data)

    def update(selfself,instance, valited_data):
        instance.user_name = valited_data.get('user_name', instance.user_name)
        instance.word = valited_data.get('word', instance.word)
        instance.image = valited_data.get('image', instance.image)

        instance.save()
        return instance
"""