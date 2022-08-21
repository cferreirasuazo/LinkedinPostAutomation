from celery import shared_task
from django.apps import apps
from django.contrib.auth.models import User

@shared_task()
def printing():
    print("HELLO WORLD")


@shared_task(bind=True)
def schedule_post(self, post_id):
    print(User)
    # Post = apps.get_model(app_label='posts', model_name='Post')
    # post = Post.objects.get(id=post_id)
    # print(post.id)
    # task_id = self.request.id
    # if (task_id):
    #     print("PUBLISH POST IN LINKEDIN")
    #     post.was_published = True
    #     post.post_url = "__POST_URL__"
    #     post.save()



    # add task_id to post 
    # update was_published to True 
    # add post_url