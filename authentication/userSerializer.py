from .models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name', 'isAdmin')
        write_only_fields = ('password',)


    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            isAdmin = validated_data['isAdmin'],
            is_staff = validated_data['isAdmin']
        )

        user.set_password(validated_data['password'])
        user.save()
        return user

