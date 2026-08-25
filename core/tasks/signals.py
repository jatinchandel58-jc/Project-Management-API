from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Task
from notification.models import Notification


@receiver(post_save, sender=Task)
def task_created_notification(sender, instance, created, **kwargs):

    if created and instance.assigned_to:
        Notification.objects.create(
            user=instance.assigned_to,
            message=f"You have been assigned a new task: {instance.title}"
        )