from unittest import defaultTestLoader
from django.db import models
import uuid
# Create your models here.


class Post(models.Model):
        id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
        text = models.TextField()
        created_at = models.DateTimeField(auto_now_add=True)
        publish_date = models.DateTimeField(default=None)
        to_publish = models.BooleanField(default=False)
        was_published = models.BooleanField(default=False)
        post_url = models.TextField(null=True, default=None, blank=True)
        

