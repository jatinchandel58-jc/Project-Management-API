from django.db import models


class Workspace(models.Model):
    user = models.ForeignKey("management.User", on_delete=models.CASCADE, related_name="workspaces")
    name = models.CharField(max_length=122, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    