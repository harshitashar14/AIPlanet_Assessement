from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse

# Create your views here.
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.exceptions import AuthenticationFailed

from authentication.userSerializer import UserSerializer
from authentication.login_serializer import LoginSerializer
from .models import User
from rest_framework_simplejwt.tokens import AccessToken


class RegisterView(APIView):
    permission_classes = [
        permissions.AllowAny  # Or anon users can't register
    ]

    def post(self, request):
        data = request.POST

        data = request.data
        serializer_class = UserSerializer(data=data)
        serializer_class.is_valid(raise_exception=True)
        user = serializer_class.save()
        return JsonResponse({
            'status': 'succeeded',
            'code': 200,
            'data': {
                'token': str(AccessToken().for_user(user)),
                'username': user.username,
            },
        })


class LoginView(APIView):
    permission_classes = [
        permissions.AllowAny  # Or anon users can't register
    ]

    def post(self, request):

        data = request.data
        serializer_class = LoginSerializer(data=data)
        serializer_class.is_valid(raise_exception=True)

        try:
            user = User.objects.get(email=serializer_class.data['email'])

        except ObjectDoesNotExist:
            raise AuthenticationFailed('User not Found! ')
        if not user.check_password(serializer_class.data['password']):
            raise AuthenticationFailed('Wrong Password !')

        return JsonResponse({
            'status': 'succeded',
            'code': 200,
            'data': {
                'token': str(AccessToken().for_user(user)),
                'username': user.username,
            },
        })
