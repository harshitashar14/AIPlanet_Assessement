import traceback

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions
from .serializers import EnrolledSerializer, SubmissionSerializer
from django.http import JsonResponse
from .models import EnrolledHackathon, Submissions
from django.core.serializers import serialize
from django_assessment.response_serializer import UserResponseSerializer, HackathonResponseSerializer, \
    SubmissionResponseSerializer, EnrolledHackathonResponseSerializer
import json


# Create your views here.
class EnrolledHackathonView(APIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]

    def post(self, request):
        data = request.data
        data['user'] = request.user.id
        validated_data = EnrolledSerializer(data=data)
        validated_data.is_valid(raise_exception=True)
        enrolled = validated_data.save()
        return JsonResponse({
            'status': 'succeded',
            'code': 200,
            'data': {
                'id': enrolled.id
            },
        })

    def get(self, request):
        data = EnrolledHackathon.objects.filter(user=request.user.id)
        output_hackathon = EnrolledHackathonResponseSerializer(data, many=True)
        data = output_hackathon.data
        return JsonResponse({
            'status': 'succeded',
            'code': 200,
            'data': data
        })


class SubmissionView(APIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]

    def post(self, request):
        data = request.data
        data['user'] = request.user.id
        validated_data = SubmissionSerializer(data=data)
        validated_data.is_valid(raise_exception=True)
        
        submission = validated_data.save()
        return JsonResponse({
            'status': 'succeded',
            'code': 200,
            'data': {
                'id': submission.id
            },
        })

    def get(self, request, id):
        data = Submissions.objects.filter(id=id)
        output_submission = SubmissionResponseSerializer(data, many=True)
        data = output_submission.data

        return JsonResponse({
            'status': 'succeded',
            'code': 200,
            'data': data,
        })


class GetEnrolledSubmissions(APIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]

    def get(self, request):
        data = Submissions.objects.filter(user=request.user.id)
        output_hackathon = EnrolledHackathonResponseSerializer(data, many=True)
        data = output_hackathon.data
        return JsonResponse({
            'status': 'succeded',
            'code': 200,
            'data': data
        })
