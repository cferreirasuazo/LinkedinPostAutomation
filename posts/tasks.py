from celery import shared_task
from django.apps import apps
from django.contrib.auth.models import User
import django
from django.conf import settings
import time

@shared_task()
def printing():
    print("HELLO WORLD")


@shared_task(bind=True, time_limit=600)
def linkedin_post(self, post_id):
    print("linkedin_post")
    Post = apps.get_model(app_label='posts', model_name='Post')
    post = Post.objects.get(id=post_id)
    task_id = self.request.id
    print(task_id)
    Post.objects.filter(pk=post_id).update(was_published=True, task_id=task_id)

    return task_id