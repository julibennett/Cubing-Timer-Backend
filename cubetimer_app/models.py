from django.db import models
from django.contrib.auth.models import User

# Add a ManyToMany field to the User model for starred users
User.add_to_class('starred_users', models.ManyToManyField(
    'self',
    through='cubetimer_app.StarredUser',
    symmetrical=False,
    related_name='starred_by_users',
    blank=True
))

class Solve(models.Model):
    solvetime = models.FloatField()
    event = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    solved_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='solves')

    def __str__(self):
        return f'{self.solvetime} seconds'

class StarredUser(models.Model):
    user = models.ForeignKey(User, related_name='user_stars', on_delete=models.CASCADE)
    starred_user = models.ForeignKey(User, related_name='starred_by', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'starred_user')
