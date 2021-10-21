from rest_framework import serializers
from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AuthUser
        fields = [
            'display_name',
            'avatar',
            'age',
            'level',
        ]


class GoogleAuth(serializers.Serializer):
    """Сериализация данных от Google"""

    email = serializers.EmailField()
    token = serializers.CharField()
