from django.urls import path
from . import views

urlpatterns = [
    path('solves/', views.SolveListCreate.as_view(), name='solve-list'),
    path('solves/<int:pk>/', views.SolveDelete.as_view(), name='solve-detail'),
]