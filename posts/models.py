from time import time
from unittest import defaultTestLoader
from django.db import models
import uuid
from .utils.Exceptions.NotValidScheduleDate import NotValidScheduleDateException
#from datetime import datetime, timedelta
import datetime
from .tasks import schedule_post
# Create your models here.


class Post(models.Model):
        id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
        text = models.TextField()
        created_at = models.DateTimeField(auto_now_add=True)
        publish_date = models.DateTimeField(default=None, null=True)
        to_publish = models.BooleanField(default=False)
        was_published = models.BooleanField(default=False)
        post_url = models.TextField(null=True, default=None, blank=True)

        def save(self, *args, **kwargs):
                time_now = datetime.datetime.now()
                publish_date = datetime.datetime(self.publish_date.year, self.publish_date. month, self.publish_date.day)
                if time_now > publish_date:
                        raise NotValidScheduleDateException(self.publish_date)
                super().save(*args, **kwargs)
                if self.to_publish:
                        post_id = str(self.id)
                        schedule_post.apply_async(args=(post_id,),countdown=5)
