from django.db import models
from django.contrib.auth.models import AbstractUser

class TwitterUser(AbstractUser):
    #don't know what properties I want yet
    favorite_color = models.CharField(max_length=20)
    a = models.IntegerField(null=True, blank=True)