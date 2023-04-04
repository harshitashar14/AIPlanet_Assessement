from django.db import models
from hackathon.models import Hackathon
from authentication.models import User


# Create your models here.
class EnrolledHackathon(models.Model):
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    hackathon = models.ForeignKey(Hackathon, null=False, on_delete=models.CASCADE)

    class Meta:
        unique_together = (("user", "hackathon"),)


class Submissions(models.Model):
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    name = models.TextField()
    hackathon = models.ForeignKey(Hackathon, null=False, on_delete=models.CASCADE)
    summary = models.TextField()
    submission_link = models.URLField(null=True, max_length=200)
    submission_image = models.ImageField(null=True, blank=True, upload_to='submission_image/')
    submission_file = models.FileField(null=True, upload_to='submission_file/')
