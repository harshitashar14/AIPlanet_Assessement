from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True)
    isAdmin = models.BooleanField(default=False)
# Create your models here.
