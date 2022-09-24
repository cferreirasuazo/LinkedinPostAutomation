from django.db.models.signals import pre_save, post_save, pre_delete
from posts.models import Post
from django.dispatch import receiver
from .task_scheduler_client import TaskSchedulerClient

@receiver(post_save, sender=Post)
def schedule_task(sender, instance, created, **kwargs):
    if created:
        TaskSchedulerClient.create_schedule_task(instance.id, instance.publish_date)

@receiver(post_save, sender=Post)
def revoke_schedule_task(sender, instance, created, **kwargs):
    if not created and not instance.to_publish and instance.task_id:
        TaskSchedulerClient.delete_schedule_task(instance.task_id)   

@receiver(pre_delete, sender=Post)
def delete_schedule_task(sender, instance,  **kwargs):
    TaskSchedulerClient.delete_schedule_task(instance.task_id)  