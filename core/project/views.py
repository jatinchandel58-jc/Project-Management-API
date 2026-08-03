from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Project
from .serializers import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return Project.objects.filter(user=self.request.user)


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)

        return Response(
            {
                "status": True,
                "message": "Project created successfully.",
                "data": serializer.data,
            },
            status=status.HTTP_201_CREATED,
        )

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        return Response(
            {
                "status": True,
                "message": "Projects retrieved successfully.",
                "count": queryset.count(),
                "data": serializer.data,
            }
        )

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        return Response(
            {
                "status": True,
                "message": "Project retrieved successfully.",
                "data": serializer.data,
            }
        )

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(
            instance,
            data=request.data,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {
                "status": True,
                "message": "Project updated successfully.",
                "data": serializer.data,
            }
        )

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(
            instance,
            data=request.data,
            partial=True,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {
                "status": True,
                "message": "Project updated successfully.",
                "data": serializer.data,
            }
        )

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()

        return Response(
            {
                "status": True,
                "message": "Project deleted successfully.",
            },
            status=status.HTTP_200_OK,
        )