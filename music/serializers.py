from rest_framework import serializers
from .models import Songs
from django.contrib.auth.models import User

class SongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields = ("id", "title", "artist")

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.artist = validated_data.get("artist", instance.artist)
        instance.save()
        return instance

class TokenSerializer(serializers.Serializer):
    """
    This serializer serializes the token data
    """
    token = serializers.CharField(max_length=255)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email")
