from django.db import models
from django.contrib.auth.models import AbstractUser

class TwitterUser(AbstractUser):
    # symmetrical makes it to where a user following someone 
    # doesn't make the user follow them back
    follows = models.ManyToManyField("self", symmetrical=False)

    def __str__(self):
        return self.username