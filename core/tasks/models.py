from django.db import models
from management.models import User
from project.models import Project

# Create your models here.

class Task(models.Model):
    STATUS_CHOICE = (
        ("completed", "Completed"),
        ("on_hold", "On_Hold"),
        ("pending", "Pending"),
        ("in_progress", "In_Progress")
    )
    PRIORITY_CHOICE = (
        ("low", "Low"),
        ("medium", "Medium"),
        ("high", "High")
    )
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="user_task", null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="user_project")
    title = models.CharField(max_length=122)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=30, choices=STATUS_CHOICE, default="pending")
    priority = models.CharField(max_length=30, choices=PRIORITY_CHOICE, default="medium")
    due_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)