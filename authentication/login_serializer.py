from .models import User
from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255, required=True)
    password = serializers.CharField(max_length=255, required=True)
    extra_kwargs = {
        'password': {'write_only': True}
    }



