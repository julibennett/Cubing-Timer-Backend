from django.urls import path
from . import views
from .views import UserSearchView, SolveChartData, UserSolveChartData, StarredUserListCreate, UnstarUser

urlpatterns = [
path('solves/', views.SolveListCreate.as_view(), name='solve-list'),
    path('solves/<int:pk>/', views.SolveDetail.as_view(), name='solve-detail'),
    path('search-users/', UserSearchView.as_view(), name='search-users'),
    path('solves/chart-data/', SolveChartData.as_view(), name='solve-chart-data'),
    path('user/<int:user_id>/chart/', UserSolveChartData.as_view(), name='user-solve-chart-data'),
    path('starred-users/', StarredUserListCreate.as_view(), name='starred-users'),
    path('unstar-user/', UnstarUser.as_view(), name='unstar-user'),
]

