from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import filters
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from .models import Workspace, WorkspaceMember
from .serializer import WorkspaceSerializer, WorkspaceMemberSerializer, WorkspaceGetSerializer


class WorkspaceViewSet(viewsets.ModelViewSet):
    serializer_class = WorkspaceSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ["name"]

    def get_queryset(self):
        return Workspace.objects.filter(user=self.request.user)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)

        return Response(
            {
                "status": True,
                "message": "Workspaces fetched successfully.",
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )

    def retrieve(self, request, *args, **kwargs):
        workspace = self.get_object()
        serializer = self.get_serializer(workspace)

        return Response(
            {
                "status": True,
                "message": "Workspace fetched successfully.",
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)

        return Response(
            {
                "status": True,
                "message": "Workspace created successfully.",
                "data": serializer.data,
            },
            status=status.HTTP_201_CREATED,
        )

    def update(self, request, *args, **kwargs):
        workspace = self.get_object()
        serializer = self.get_serializer(workspace, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {
                "status": True,
                "message": "Workspace updated successfully.",
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )

    def partial_update(self, request, *args, **kwargs):
        workspace = self.get_object()
        serializer = self.get_serializer(
            workspace,
            data=request.data,
            partial=True,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {
                "status": True,
                "message": "Workspace updated successfully.",
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )

    def destroy(self, request, *args, **kwargs):
        workspace = self.get_object()
        workspace.delete()

        return Response(
            {
                "status": True,
                "message": "Workspace deleted successfully.",
            },
            status=status.HTTP_200_OK,
        )

class CreateMemberView(APIView):
    permission_classes = [IsAuthenticated]
    #GET /api/workspaces/<workspace_id>/members/
    def get(self, request, workspace_id):
        workspace = get_object_or_404(
            Workspace,
            id=workspace_id
        )
        queryset = WorkspaceMember.objects.filter(workspace=workspace)
        serializer = WorkspaceGetSerializer(queryset, many=True)
        return Response({
            "Message": "All Member Data",
            "Data": serializer.data
        })

    def post(self, request):
        serializer = WorkspaceMemberSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "Message": "Your Create a member for workspace",
            "Data": serializer.data
        })

class GetMemberView(APIView):
    def get(self, request, workspace_id, member_id):
        queryset = get_object_or_404(
            WorkspaceMember,
            id= member_id,
            workspace_id=workspace_id
        )
        serializer = WorkspaceGetSerializer(queryset)
        return Response({
            "status": True,
            "Message": "Member of the workspace",
            "Data": serializer.data
        })