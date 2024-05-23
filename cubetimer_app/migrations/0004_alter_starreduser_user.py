# Generated by Django 4.2.13 on 2024-05-23 03:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cubetimer_app', '0003_starreduser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='starreduser',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_stars', to=settings.AUTH_USER_MODEL),
        ),
    ]
