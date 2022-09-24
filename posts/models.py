from time import time
from unittest import defaultTestLoader
from django.db import models
import uuid
from .utils.Exceptions.NotValidScheduleDate import NotValidScheduleDateException
#from datetime import datetime, timedelta
import datetime
from .task_scheduler_client import TaskSchedulerClient
from accounts.models import CoreUser
# Create your models here.

class PostManager(models.Manager):
    def update_post(self, instance, update_attr):
        obj, created = self.update_or_create(id=instance.pk, defaults=update_attr)
        return obj

    def delete_post(self, post_id):
        post = self.get(id = post_id)
        post.delete()

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    publish_date = models.DateTimeField(default=None, null=True)
    to_publish = models.BooleanField(default=False)
    was_published = models.BooleanField(default=False)
    post_url = models.TextField(null=True, default=None, blank=True)
    task_id = models.TextField(null=True, default=None, blank=True)
    user = models.ForeignKey(CoreUser, on_delete=models.CASCADE)

    objects = PostManager()

    def save(self, *args, **kwargs):
        # time_now = datetime.datetime.now()
        # publish_date = datetime.datetime(self.publish_date.year, self.publish_date. month, self.publish_date.day)
        # if time_now > publish_date:
        #         raise NotValidScheduleDateException(self.publish_date)
        super().save(*args, **kwargs)


        # if not self._state.adding:
        #     if not self.to_publish:
        #         print("KILL TASK")
        #         print("REMOVE TASK ID")
        # if self.to_publish:
        #     print("SCHEDULE POST")
        #     task_id = linkedin_post.apply_async(args=(post_id,), countdown=100)
        #     print(f"schedule task {task_id}")
        #     self.task_id = task_id
        #     linkedin_post.apply_async(args=(post_id,),eta=self.publish_date)