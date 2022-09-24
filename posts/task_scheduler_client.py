from postautomation.celery import app
from posts.tasks import share_post
from django.apps import apps


class TaskSchedulerClient():
    @classmethod
    def delete_schedule_task(self, task_id):
        app.control.revoke(task_id, terminate=True)

    @classmethod
    def create_schedule_task(self, post_id, publish_date):
        print("create schedule task")
        print(f"schedule date {publish_date}")
        Post = apps.get_model(app_label='posts', model_name='Post')
        task_id = share_post.apply_async(args=(post_id,), eta=publish_date)
        post = Post.objects.get(id=post_id)
        Post.objects.update_post(post, {"task_id": task_id.id})