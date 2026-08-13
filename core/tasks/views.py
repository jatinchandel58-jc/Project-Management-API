from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied

from .models import Task
from .serializers import TaskSerializer
from .permissions import IsTaskOwnerOrAssignee


class TaskViewSet(viewsets.ModelViewSet):

    serializer_class = TaskSerializer

    permission_classes = [
        IsAuthenticated,
        IsTaskOwnerOrAssignee
    ]

    def get_queryset(self):
        user = self.request.user

        if Task.objects.filter(
            project__workspace__user=user
        ).exists():

            return Task.objects.filter(
                project__workspace__user=user
            )

        return Task.objects.filter(
            assigned_to=user
        )

    # GET all tasks
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        return Response({
            "status": True,
            "message": "Tasks fetched successfully.",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    # GET one task
    def retrieve(self, request, *args, **kwargs):
        task = self.get_object()
        serializer = self.get_serializer(task)

        return Response({
            "status": True,
            "message": "Task fetched successfully.",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    # POST create task
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        project = serializer.validated_data["project"]

        if project.workspace.user != request.user:
            raise PermissionDenied(
                "Only the workspace owner can create and assign tasks."
            )

        serializer.save()

        return Response({
            "status": True,
            "message": "Task created successfully.",
            "data": serializer.data
        }, status=status.HTTP_201_CREATED)

    # PUT
    def update(self, request, *args, **kwargs):
        task = self.get_object()

        serializer = self.get_serializer(
            task,
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            "status": True,
            "message": "Task updated successfully.",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    # PATCH
    def partial_update(self, request, *args, **kwargs):
        task = self.get_object()

        serializer = self.get_serializer(
            task,
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            "status": True,
            "message": "Task partially updated successfully.",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    # DELETE
    def destroy(self, request, *args, **kwargs):
        task = self.get_object()
        task.delete()

        return Response({
            "status": True,
            "message": "Task deleted successfully."
        }, status=status.HTTP_200_OK)