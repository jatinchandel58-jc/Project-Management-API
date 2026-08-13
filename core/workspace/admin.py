from django.contrib import admin
from .models import Workspace , WorkspaceMember

@admin.register(Workspace)
class WorkspaceAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "user",
        "created_at",
        "updated_at",
    )

    search_fields = (
        "name",
        "description",
        "user__email",
    )

    list_filter = (
        "created_at",
        "updated_at",
    )

    ordering = (
        "-created_at",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    fieldsets = (
        (
            "Workspace Information",
            {
                "fields": (
                    "user",
                    "name",
                    "description",
                )
            },
        ),
        (
            "Timestamps",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                )
            },
        ),
    )

@admin.register(WorkspaceMember)
class MemberAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "workspace", "joined_at")