from celery import shared_task

@shared_task
def printing():
    print("HELLO WORLD CELERY")


@shared_task
def schedule_post(post):
    print(post.id)



