from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Solve, Friendship

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

class FriendshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friendship
        fields = ['id', 'creator', 'friend', 'created_at']
        read_only_fields = ('creator', 'created_at')  # 'creator' and 'created_at' should not be set by the user

    def validate(self, data):
        if data['friend'] == self.context['request'].user:
            raise serializers.ValidationError("Users cannot be friends with themselves.")
        return data

    def create(self, validated_data):
        validated_data['creator'] = self.context['request'].user
        return Friendship.objects.create(**validated_data)