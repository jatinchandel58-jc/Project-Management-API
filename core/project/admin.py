from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "user",
        "workspace",
        "status",
        "start_date",
        "end_date",
        "created_at",
    )

    search_fields = (
        "name",
        "description",
        "user__email",
        "workspace__name",
    )

    list_filter = (
        "status",
        "start_date",
        "end_date",
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
            "Project Information",
            {
                "fields": (
                    "user",
                    "workspace",
                    "name",
                    "description",
                    "status",
                )
            },
        ),
        (
            "Project Timeline",
            {
                "fields": (
                    "start_date",
                    "end_date",
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