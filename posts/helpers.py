from celery import shared_task

def update_post(post_id):
    from .models import Post
    post = Post.objects.get(id=post_id)
    
