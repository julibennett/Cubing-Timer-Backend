from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Solve, Profile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
class SolveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solve
        fields = ['id', 'solvetime', 'event', 'date', 'solved_by']
        extra_kwargs = {'solved_by': {'read_only': True}}

class ProfileSerializer(serializers.ModelSerializer):
    friends = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all())

    class Meta:
        model = Profile
        fields = ['user', 'bio', 'friends']