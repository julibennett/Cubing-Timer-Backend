from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

class Solve(models.Model):
    solvetime = models.FloatField()
    event = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    solved_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='solves')

    def __int__(self):
        return self.solvetime

class StarredUser(models.Model):
    user = models.ForeignKey(User, related_name='starred_users', on_delete=models.CASCADE)
    starred_user = models.ForeignKey(User, related_name='starred_by', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'starred_user')