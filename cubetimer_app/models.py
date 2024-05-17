from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.conf import settings

class CustomUser(AbstractUser):
    friends = models.ManyToManyField('self', through='Friendship', symmetrical=False, related_name='friends+')


class Solve(models.Model):
    solvetime = models.FloatField()
    event = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    solved_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='solves')

    def __int__(self):
        return self.solvetime


class Friendship(models.Model):
    from_user = models.ForeignKey(CustomUser, related_name='friendships', on_delete=models.CASCADE)
    to_user = models.ForeignKey(CustomUser, related_name='+', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['from_user', 'to_user'], name='unique_friendship')
        ]

    def __str__(self):
        return f"{self.from_user.username} is friends with {self.to_user.username}"