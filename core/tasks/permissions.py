from rest_framework.permissions import BasePermission


class IsTaskOwnerOrAssignee(BasePermission):

    def has_object_permission(self, request, view, obj):

        # Workspace owner can do everything
        if obj.project.workspace.user == request.user:
            return True

        # Members can update their own assigned tasks
        if request.method in ["PUT", "PATCH"]:
            if obj.assigned_to == request.user:
                return True

        return False