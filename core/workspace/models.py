from django.db import models


class Workspace(models.Model):
    user = models.ForeignKey("management.User", on_delete=models.CASCADE, related_name="workspaces")
    name = models.CharField(max_length=122, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class WorkspaceMember(models.Model):
    workspace = models.ForeignKey(
        Workspace,
        on_delete=models.CASCADE,
        related_name="members"
    )
    user = models.ForeignKey(
        "management.User",
        on_delete=models.CASCADE,
        related_name="workspace_memberships"
    )
    role = models.CharField(
        max_length=20,
        choices=[
            ("member", "Member"),
            ("admin", "Admin"),
        ],
        default="member"
    )
    joined_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.workspace.name 