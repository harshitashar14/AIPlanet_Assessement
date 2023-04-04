from .models import Hackathon, Favourites
from authentication.models import User
from rest_framework import serializers


class HackathonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hackathon
        fields = ('name', 'summary', 'description', 'creator', 'reward_prize', 'repo_link', 'other_links',
                  'cover_image', 'bg_image', 'start_date', 'end_date', 'submission_type')

    def create(self, validated_data):
        hackathon = Hackathon.objects.create(
            name=validated_data['name'],
            summary=validated_data['summary'],
            description=validated_data['description'],
            reward_prize=validated_data['reward_prize'],
            repo_link=validated_data['repo_link'],
            other_links=validated_data['other_links'],
            cover_image=validated_data['cover_image'],
            bg_image=validated_data['bg_image'],
            start_date=validated_data['start_date'],
            end_date=validated_data['end_date'],
            submission_type=validated_data['submission_type'],
            creator=validated_data['creator']

        )

        hackathon.save()
        return hackathon


class FavouritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favourites
        fields = ('admin', 'hackathon')

    def create(self, validated_data):
        try:
            favourites = Favourites.objects.create(
                admin=validated_data['admin'],
                hackathon=validated_data['hackathon'],
            )
        except:
            print("jvjfvj")

        favourites.save()
        return favourites
