from django.conf import settings
from django.db import models
from model_utils.models import SoftDeletableModel, TimeStampedModel


class Follower(TimeStampedModel, SoftDeletableModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="follower")
    follow_to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="follow_to")
    get_notification = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user} is following {self.follow_to}"