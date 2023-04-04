from rest_framework import serializers
from .models import EnrolledHackathon, Submissions
from hackathon.models import SubmissionType
from rest_framework.exceptions import ValidationError
import datetime

class EnrolledSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnrolledHackathon
        fields = ('user', 'hackathon')

    def create(self, validated_data):
        enrolled = EnrolledHackathon.objects.create(
            user=validated_data['user'],
            hackathon=validated_data['hackathon'],
        )
        enrolled.save()
        return enrolled


class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submissions
        fields = ('user', 'name', 'hackathon', 'summary', 'submission_link', 'submission_image', 'submission_file')

    def create(self, validated_data):
        submission_type = validated_data['hackathon'].submission_type
        end_date = validated_data['hackathon'].end_date
        start_date = validated_data['hackathon'].start_date
        today = datetime.date.today()
        if start_date > today:
            raise ValidationError("Hackathon has not started.")
        if end_date < today:
            raise ValidationError("Hackathon ended.")
        submission = Submissions(
            user=validated_data['user'],
            hackathon=validated_data['hackathon'],
            name=validated_data['name'],
            summary=validated_data['summary']
        )
        if submission_type == SubmissionType.LINK:
            if not validated_data.__contains__('submission_link'):
                raise ValidationError("submission type incompatible")
            else:
                submission.submission_link = validated_data['submission_link']
        if submission_type == SubmissionType.IMAGE:
            if not validated_data.__contains__('submission_image'):
                raise ValidationError("submission type incompatible")
            else:
                submission.submission_image = validated_data['submission_image']
        if submission_type == SubmissionType.FILE:
            if not validated_data.__contains__('submission_file'):
                raise ValidationError("submission type incompatible")
            else:
                submission.submission_file = validated_data['submission_file']

        submission.save()
        return submission
