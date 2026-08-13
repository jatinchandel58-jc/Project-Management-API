from rest_framework import serializers
from .models import Task
from project.models import Project
from workspace.models import WorkspaceMember


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = [
            "id",
            "project",
            "assigned_to",
            "title",
            "description",
            "status",
            "priority",
            "due_date",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
        ]

    def validate_title(self, value):
        if value.strip() == "":
            raise serializers.ValidationError(
                "Please fill the title."
            )

        return value

    def validate_assigned_to(self, value):
        project_id = self.initial_data.get("project")

        if not project_id:
            return value

        project = Project.objects.get(id=project_id)

        is_member = WorkspaceMember.objects.filter(
            workspace=project.workspace,
            user=value
        ).exists()

        if not is_member:
            raise serializers.ValidationError(
                "This user is not a member of the project workspace."
            )

        return value