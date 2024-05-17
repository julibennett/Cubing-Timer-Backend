from django.urls import path
from . import views
from .views import UserSearchView, AddFriendView, ProfileView, UpdateProfile, ListFriends

urlpatterns = [
    path('solves/', views.SolveListCreate.as_view(), name='solve-list'),
    path('solves/<int:pk>/', views.SolveDetail.as_view(), name='solve-detail'),
    path('search-users/', UserSearchView.as_view(), name='search-users'),
    path('add-friend/', AddFriendView.as_view(), name='add-friend'),
    path('profile/', ProfileView.as_view(), name='profile-view'),  # View a user's profile
    path('profile/update/', UpdateProfile.as_view(), name='update-profile'),  # Update a user's profile
    path('profile/friends/', ListFriends.as_view(), name='list-friends'),  # List a user's friends
]