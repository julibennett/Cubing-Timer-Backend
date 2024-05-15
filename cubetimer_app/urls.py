from django.urls import path
from . import views
from .views import UserSearchView, AddFriendView

urlpatterns = [
    path('solves/', views.SolveListCreate.as_view(), name='solve-list'),
    path('solves/<int:pk>/', views.SolveDetail.as_view(), name='solve-detail'),
    path('search-users/', UserSearchView.as_view(), name='search-users'),
    path('add-friend/', AddFriendView.as_view(), name='add-friend'),
]