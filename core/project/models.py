from django.db import models

class Project(models.Model):
    PROJECT_STATUS = (
        ("planning", "Planning"),
        ("in_progress", "In Progress"),
        ("completed", "Completed"),
        ("on_hold", "On Hold"),
    )
    user = models.ForeignKey("management.User", on_delete=models.CASCADE, related_name="projects")
    workspace = models.ForeignKey("workspace.Workspace", on_delete=models.CASCADE, related_name="projects")
    name = models.CharField(max_length=122, unique=True)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=122, choices=PROJECT_STATUS, default="planning")
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
