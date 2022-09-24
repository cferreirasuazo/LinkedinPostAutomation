from urllib import response
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse

from .forms import PostForm
from posts.models import Post
from .clients.LinkedinManager import LinkedinManager
import requests
import json


def linkedin(request):
    linkedinManager = LinkedinManager()
    authorization_code = request.GET.get("code")
    linkedinManager.set_authorization_code(authorization_code)
    token = linkedinManager.get_access_token()
    return HttpResponse(json.dumps(token))


def login(request):
    return render(request, "posts/auth/login.html")


def signup(request):
    return render(request, "posts/auth/signup.html")


def forget_password(request):
    return render(request, "posts/auth/forget_password.html")


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
    return render(request, 'posts/index.html', context)
