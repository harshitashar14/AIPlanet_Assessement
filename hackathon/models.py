from django.db import models
from django.db.models import UniqueConstraint

from authentication.models import User


# Create your models here.
class SubmissionType(models.TextChoices):
    IMAGE = 'image'  # png jpg jpeg
    FILE = 'file'  # txt
    LINK = 'link'


class Hackathon(models.Model):
    name = models.TextField(max_length=50)
    summary = models.TextField(max_length=9000)
    description = models.TextField(max_length=9000, null=True)
    creator = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    reward_prize = models.IntegerField(default=0)
    repo_link = models.URLField(max_length=200)
    other_links = models.URLField(max_length=200)
    bg_image = models.ImageField(upload_to='uploads/')
    cover_image = models.ImageField(upload_to='uploads/')
    start_date = models.DateField()
    end_date = models.DateField()

    submission_type = models.CharField(
        max_length=32,
        choices=SubmissionType.choices,
        default=SubmissionType.FILE,
    )

    def __str__(self):
        return self.name


class Favourites(models.Model):

    admin = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    hackathon = models.ForeignKey(Hackathon, null=False, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['admin', 'hackathon'], name='unique_host_migration'),
        ]
