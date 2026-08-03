from rest_framework import serializers
from .models import Project
from workspace.models import Workspace

class ProjectSerializer(serializers.ModelSerializer):
    workspace = serializers.SlugRelatedField(
        queryset=Workspace.objects.all(),
        slug_field="name"
    )

    class Meta:
        model = Project
        fields = [
            "id",
            "workspace",
            "name",
            "description",
            "status",
            "start_date",
            "end_date",
            "created_at",
            "updated_at"
        ]

        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
        ]

    def validate_name(self, obj):
        if obj.strip() == "":
            raise serializers.ValidationError(
                "Project name cannot be empty."
            )
        return obj

    def validate(self, data):
        start_date = data.get(
            "start_date",
            self.instance.start_date if self.instance else None
        )

        end_date = data.get(
            "end_date",
            self.instance.end_date if self.instance else None
        )

        if start_date and end_date:
            if start_date > end_date:
                raise serializers.ValidationError(
                    "End date must be after start date."
                )

        return data