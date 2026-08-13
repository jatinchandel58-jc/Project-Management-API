from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

routers = DefaultRouter()
routers.register("task", TaskViewSet, basename="task")

urlpatterns = routers.urls