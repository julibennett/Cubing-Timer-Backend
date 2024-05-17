from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.conf import settings

class CustomUser(AbstractUser):
    friends = models.ManyToManyField('self', symmetrical=True, related_name='my_friends', blank=True)

class Solve(models.Model):
    solvetime = models.FloatField()
    event = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    solved_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='solves')

    def __int__(self):
        return self.solvetime
