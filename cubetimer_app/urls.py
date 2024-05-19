from django.urls import path
from . import views
from .views import UserSearchView, ProfileView, UpdateProfile, ListFriends, AddFriendView, SolveChartData

urlpatterns = [
path('solves/', views.SolveListCreate.as_view(), name='solve-list'),
    path('solves/<int:pk>/', views.SolveDetail.as_view(), name='solve-detail'),
    path('search-users/', UserSearchView.as_view(), name='search-users'),
    path('profile/', ProfileView.as_view(), name='profile-view'),  
    path('profile/update/', UpdateProfile.as_view(), name='update-profile'),  
    path('profile/friends/', ListFriends.as_view(), name='list-friends'),
    path('add-friend/', AddFriendView.as_view(), name='add-friend'),
    path('solves/chart-data/', SolveChartData.as_view(), name='solve-chart-data'),
]
