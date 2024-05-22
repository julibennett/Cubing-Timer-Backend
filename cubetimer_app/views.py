from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from rest_framework import generics, permissions, status, serializers
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from .serializers import UserSerializer, SolveSerializer, StarredUserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Solve, StarredUser
from rest_framework.response import Response
from rest_framework.views import APIView

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
        serializer.save()

class UserSearchView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        username = self.request.query_params.get('username', None)
        if username is not None:
            return User.objects.filter(username__icontains=username)
        return User.objects.none()

class SolveChartData(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        solves = Solve.objects.filter(solved_by=request.user)
        serializer = SolveSerializer(solves, many=True)
        return Response(serializer.data)
    
class UserSolveChartData(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        solves = Solve.objects.filter(solved_by=user)
        serializer = SolveSerializer(solves, many=True)
        return Response(serializer.data)
    
class StarredUserListCreate(generics.ListCreateAPIView):
    serializer_class = StarredUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return StarredUser.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        if StarredUser.objects.filter(user=self.request.user, starred_user_id=serializer.validated_data['starred_user'].id).exists():
            raise serializers.ValidationError("User already starred.")
        serializer.save(user=self.request.user)

class UnstarUser(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        starred_user_id = request.data.get('starred_user_id')
        try:
            starred_user = StarredUser.objects.get(user=request.user, starred_user_id=starred_user_id)
            starred_user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except StarredUser.DoesNotExist:
            return Response({"error": "Starred user not found."}, status=status.HTTP_404_NOT_FOUND)
    
# class UserDetailView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         serializer = UserSerializer(request.user)
#         return Response(serializer.data)
