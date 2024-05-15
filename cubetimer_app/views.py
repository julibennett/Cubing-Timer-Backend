from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from .serializers import UserSerializer, SolveSerializer, FriendshipSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Solve, Friendship

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

class UserSearchView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        username = self.request.query_params.get('username', None)
        if username is not None:
            return User.objects.filter(username__icontains=username)
        return User.objects.none()

class AddFriendView(generics.CreateAPIView):
    serializer_class = FriendshipSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)