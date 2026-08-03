from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet

routers = DefaultRouter()
routers.register("project", ProjectViewSet, basename="project")

urlpatterns = routers.urls