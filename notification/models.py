from django.db import models
from twitteruser.models import TwitterUser

class Notification(models.Model):
    sender = models.ForeignKey(TwitterUser, on_delete=models.CASCADE, null=True, related_name='sender_notification')
    recipient = models.ForeignKey(TwitterUser, on_delete=models.CASCADE, related_name='recipient_notification')
    message = models.TextField()
    read = models.BooleanField(default=False)