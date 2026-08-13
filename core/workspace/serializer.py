from rest_framework import serializers
from .models import Workspace, WorkspaceMember
from management.models import User


class WorkspaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workspace
        fields = [
            "id",
            "name",
            "description",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
        ]

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError(
                "Workspace name cannot be empty."
            )

        return value

class WorkspaceMemberSerializer(serializers.ModelSerializer):
    workspace = serializers.PrimaryKeyRelatedField(
        queryset=Workspace.objects.all()
    )
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all()
    )

    class Meta:
        model = WorkspaceMember
        fields = [
            "id",
            "workspace",
            "user",
            "role",
            "joined_at",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "joined_at",
            "created_at",
            "updated_at",
        ]
    def validate(self, attrs):
        workspace = attrs.get("workspace")
        user = attrs.get("user")

        if WorkspaceMember.objects.filter(
            workspace=workspace,
            user=user
        ).exists():
            raise serializers.ValidationError(
                "User is already in workspace"
            )

        return attrs

class WorkspaceGetSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.first_name")
    workspace = serializers.CharField(source="workspace.name")
    class Meta:
        model = WorkspaceMember
        fields = [
            "id",
            "workspace",
            "user",
            "role",
            "joined_at",
            "created_at",
            "updated_at",
        ]