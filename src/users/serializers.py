from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'id', 'first_name',
                  'last_name', 'image', 'level', 'age', 'courses', 'lessons')
