from celery import shared_task
from django.apps import apps
from django.contrib.auth.models import User
import django
from django.conf import settings
import time
from datetime import datetime
@shared_task(bind=True, time_limit=600)
def share_post(self, post_id):
    Post = apps.get_model(app_label='posts', model_name='Post')
    print(datetime.now())
    task_id = self.request.id
    schedule_task = {
        "was_published": True,
    }
    post = Post.objects.get(id=post_id)
    Post.objects.update_post(post, schedule_task)
    return task_id