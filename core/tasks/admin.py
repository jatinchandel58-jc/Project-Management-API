from django.contrib import admin
from .models import Task

@admin.register(Task)
class NotificationAdmin(admin.ModelAdmin):
    list_display= ["id", "title", "status", "priority"]