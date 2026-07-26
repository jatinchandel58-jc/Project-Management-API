from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WorkspaceViewSet

routers = DefaultRouter()
routers.register("workspace", WorkspaceViewSet, basename="workspace")

urlpatterns = routers.urls