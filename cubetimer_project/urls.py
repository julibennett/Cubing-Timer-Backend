from django.contrib import admin
from django.urls import path, include
from cubetimer_app.views import CreateUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/user/register/", CreateUserView.as_view(), name="register"),
    path("api/token/", TokenObtainPairView.as_view(), name="get_token"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="refresh"),
    path("api-auth/", include("rest_framework.urls")),
    path('api/', include('cubetimer_app.urls')),
]

# curl -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE2MDg1MDcxLCJpYXQiOjE3MTYwNzc4NzEsImp0aSI6IjUyMDMxMDRkNjIwODQ4NWY5ODBmYjJjZDI0NWQ3MjNlIiwidXNlcl9pZCI6Mn0.0xbpjM4j5XTbo1svmhgDsbK1sC48tGhWFE9MPJuvtVM" http://127.0.0.1:8000/api/profile/
#