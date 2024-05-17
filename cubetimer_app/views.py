from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from .serializers import UserSerializer, SolveSerializer, ProfileSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Solve, Profile

class SolveListCreate(generics.ListCreateAPIView):
    serializer_class = SolveSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Solve.objects.filter(solved_by=user)
    
    def perform_create(self, serializer):
        serializer.save(solved_by=self.request.user)


class SolveDetail(RetrieveUpdateDestroyAPIView):
    queryset = Solve.objects.all()
    serializer_class = SolveSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Solve.objects.filter(solved_by=user)
    

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save()
        Profile.objects.create(user=user)

class UserSearchView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        username = self.request.query_params.get('username', None)
        if username is not None:
            return User.objects.filter(username__icontains=username)
        return User.objects.none()

class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.profile

class UpdateProfile(generics.UpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.profile

class ListFriends(generics.ListAPIView):
    serializer_class = UserSerializer  
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.request.user.profile.friends.all()