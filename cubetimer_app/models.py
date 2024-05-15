from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Solve(models.Model):
    solvetime = models.FloatField()
    event = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    solved_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='solves')

    def __int__(self):
        return self.solvetime


class Friendship(models.Model):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='friendship_creator', on_delete=models.CASCADE)
    friend = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='friendship_friend', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['creator', 'friend'], name='unique_friendship')
        ]