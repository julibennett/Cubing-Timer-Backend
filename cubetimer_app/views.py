from django.contrib.auth.models import User
from rest_framework import generics, permissions, status
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, SolveSerializer
from .models import Solve, StarredUser

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
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        username = self.request.query_params.get('username', None)
        if username is not None:
            return User.objects.filter(username__icontains=username)
        return User.objects.none()

class UserSolveChartData(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, user_id):
        try:
            user = User.objects.get(pk=user_id)
            solves = Solve.objects.filter(solved_by=user)
            serializer = SolveSerializer(solves, many=True)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

class StarredUserListCreate(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.request.user.starred_users.all()

    def create(self, request, *args, **kwargs):
        starred_user_id = request.data.get('starred_user')
        try:
            starred_user = User.objects.get(pk=starred_user_id)
            StarredUser.objects.create(user=request.user, starred_user=starred_user)
            return Response({"status": "User starred successfully"}, status=status.HTTP_201_CREATED)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class UnstarUser(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        starred_user_id = request.data.get('starred_user_id')
        try:
            starred_user = User.objects.get(pk=starred_user_id)
            StarredUser.objects.filter(user=request.user, starred_user=starred_user).delete()
            return Response({"status": "User unstarred successfully"}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class SolveChartData(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        solves = Solve.objects.filter(solved_by=request.user)
        serializer = SolveSerializer(solves, many=True)
        return Response(serializer.data)
