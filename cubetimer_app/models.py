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

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True)
    friends = models.ManyToManyField('self', symmetrical=True, blank=True, related_name='friend_set')

    def __str__(self):
        return f'{self.user.username}\'s profile'