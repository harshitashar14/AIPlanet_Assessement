from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from .serializers import HackathonSerializer, FavouritesSerializer
# Create your views here.
from rest_framework.views import APIView
from rest_framework import permissions
from .models import Hackathon, Favourites
from django_assessment.response_serializer import HackathonResponseSerializer, FavouriteHackathonResponseSerializer


class CreateHackathonView(APIView):
    permission_classes = [
        permissions.IsAdminUser  # Or anon users can't register
    ]

    def post(self, request):
        data = request.data
        data['creator'] = request.user.id
        validated_data = HackathonSerializer(data=data)
        validated_data.is_valid(raise_exception=True)
        hackathon = validated_data.save()
        return JsonResponse({
            'status': 'succeded',
            'code': 200,
            'data': {
                'id': hackathon.id
            },
        })


class GetAdminHackathonView(APIView):
    permission_classes = [
        permissions.IsAdminUser  # Or anon users can't register
    ]

    def get(self, request):
        data = Hackathon.objects.filter(creator=request.user.id)
        output_hackathon = HackathonResponseSerializer(data, many=True)
        data = output_hackathon.data
        return JsonResponse({
            'status': 'succeded',
            'code': 200,
            'data': data
        })


class GetHackathonView(APIView):
    permission_classes = [
        permissions.AllowAny  # Or anon users can't register
    ]

    def get(self, request):
        data = Hackathon.objects.all()
        output_hackathon = HackathonResponseSerializer(data, many=True)
        data = output_hackathon.data
        return JsonResponse({
            'status': 'succeded',
            'code': 200,
            'data': data
        })


class GetHackathonByIdView(APIView):
    permission_classes = [
        permissions.AllowAny  # Or anon users can't register
    ]

    def get(self, request, id):
        data = Hackathon.objects.filter(id=id)
        output_hackathon = HackathonResponseSerializer(data, many=True)
        data = output_hackathon.data
        return JsonResponse({
            'status': 'succeded',
            'code': 200,
            'data': data
        })


class MakeFavouritesView(APIView):
    permission_classes = [
        permissions.IsAdminUser  # Or anon users can't register
    ]

    def post(self, request):
        data = request.data
        data['admin'] = request.user.id
        validated_data = FavouritesSerializer(data=data)
        validated_data.is_valid(raise_exception=True)
        favourite = validated_data.save()
        return JsonResponse({
            'status': 'succeded',
            'code': 200,
            'data': {
                'id': favourite.id
            },
        })


class GetAllFavouriteView(APIView):
    permission_classes = [
        permissions.IsAdminUser  # Or anon users can't register
    ]

    def get(self, request):
        data = Favourites.objects.filter(admin=request.user.id)
        output_hackathon = FavouriteHackathonResponseSerializer(data, many=True)
        data = output_hackathon.data
        return JsonResponse({
            'status': 'succeded',
            'code': 200,
            'data': data
        })
