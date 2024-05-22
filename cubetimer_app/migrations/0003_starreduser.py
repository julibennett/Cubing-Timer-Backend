# Generated by Django 4.2.13 on 2024-05-22 21:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cubetimer_app', '0002_delete_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='StarredUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starred_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='starred_by', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='starred_users', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'starred_user')},
            },
        ),
    ]