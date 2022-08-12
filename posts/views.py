from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import PostForm
from posts.models import Post

def index(request):
    
    posts = Post.objects.all()

    if request.method != 'POST':
        form = PostForm()
    else:
        form = PostForm(data=request.POST)
        if form.is_valid():
            form.save()
            form = PostForm()
            HttpResponseRedirect(reverse('posts:index'))

    context = {"form": form, 'posts': posts}
    return render(request, 'posts/index.html',context)


# Create your views here.
