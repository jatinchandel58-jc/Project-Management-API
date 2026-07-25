from django.contrib import admin
from django.urls import path, include
from .views import (
    RegisterView,
    LoginViewSet,
    ProfileView,
    ChangePassword,
    LogoutView
)
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("register/", RegisterView.as_view()),
    path("login/", LoginViewSet.as_view()),
    path("change-password/", ChangePassword.as_view()),
    path("profile/", ProfileView.as_view()),
    path("logout/", LogoutView.as_view())
]
