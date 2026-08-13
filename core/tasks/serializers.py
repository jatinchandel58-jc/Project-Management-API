from rest_framework import serializers
from .models import Task

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

    def validate_title(self, attrs):
        if attrs.strip() == "":
            raise serializers.ValidationError(
                "Please fill the title "
            )
        return attrs

    def validate(self, data):
        project = data.get(
            "project",
            self.instance.project if self.instance else None)
        due_date = data.get(
            "due_date",
            self.instance.due_date if self.instance else None
            )

        if project and due_date:
            if due_date < project.start_date:
                raise serializers.ValidationError(
                    "Task due date cannot be before project start date."
                )

        return data

    # def validate_project(self, value):
    #     request = self.context.get("request")

    #     if request and value.user != request.user:
    #         raise serializers.ValidationError(
    #             "You can only create tasks in your own projects."
    #         )

    #     return value
