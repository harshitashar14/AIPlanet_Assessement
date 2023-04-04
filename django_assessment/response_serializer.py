from rest_framework import serializers
from authentication.models import User
from hackathon.models import Hackathon, Favourites
from submissions.models import Submissions, EnrolledHackathon


class UserResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username','first_name','last_name')


class HackathonResponseSerializer(serializers.ModelSerializer):
    creator = UserResponseSerializer()

    class Meta:
        model = Hackathon
        fields = '__all__'
        related_object = 'creator'


class EnrolledHackathonResponseSerializer(serializers.ModelSerializer):
    user = UserResponseSerializer()
    hackathon = HackathonResponseSerializer()

    class Meta:
        model = EnrolledHackathon
        fields = ('user', 'hackathon')
        related_object = 'user', 'hackathon'


class SubmissionResponseSerializer(serializers.ModelSerializer):
    hackathon = HackathonResponseSerializer()

    class Meta:
        model = Submissions
        fields = ('user', 'name', 'hackathon', 'summary', 'submission_link', 'submission_image', 'submission_file')


class FavouriteHackathonResponseSerializer(serializers.ModelSerializer):
    admin = UserResponseSerializer()
    hackathon = HackathonResponseSerializer()

    class Meta:
        model = Favourites
        fields = ('admin', 'hackathon')
        related_object = 'admin', 'hackathon'
