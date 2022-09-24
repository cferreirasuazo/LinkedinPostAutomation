from csv import excel
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import UpdateAPIView, RetrieveAPIView, RetrieveAPIView, CreateAPIView
from posts.models import Post
from .serializer import PostSerializer
from posts.utils.Exceptions import NotValidScheduleDate
from posts.tasks import share_post
from postautomation.celery import app
from accounts.models import CoreUser
from django.contrib.auth import authenticate
from accounts.serializers import UserSerializer




class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class CancelScheduleTask(UpdateAPIView):
    def patch(self, request,id):
        try:
            post = Post.objects.get(id=id)
            serializer = PostSerializer(post)
        except Post.DoesNotExist:
            return Response({"message":"Post not found"}, status=404)
        except Exception:
            return Response({"message": "Error"}, status=500)
        return Response(serializer.data, status=200)

class PublishPost(UpdateAPIView ):
    def patch(self,request, id):
        try:
            post = Post.objects.get(id=id)
            post.to_publish = True
            share_post.apply_async(args=(id,), countdown=240 )
            post.save()
            serializer = PostSerializer(post)
        except Exception: 
            return Response({"message": "Error"}, status=500)
        except NotValidScheduleDate:
            return Response({"message": "Invalid schedule date"}, status=500)
        except Post.DoesNotExist:
            return Response({"message":"Post not found"}, status=404)

        return Response(serializer.data, status=200)


class UserPosts(RetrieveAPIView):
    def get(self, request,user_id):
        try:
            posts = CoreUser.objects.user_posts(user_id)
        except CoreUser.DoesNotExist:
            return Response({"message": "User does not exist"}, status=404) 
        
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=200)





class UserSignUpView(CreateAPIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.create(data=request.data)
        else:
            return Response(serializer.errors,status=500)       
        
        user = CoreUser.objects.get(email=request.data.get("email"))
        serializer = UserSerializer(user)
        return Response(serializer.data,status=201)
        

class UserSignInView(RetrieveAPIView):
    def post(self,request):
        email = request.data.get("email")
        password = request.data.get("password")
        try:
            user = CoreUser.objects.get(email=email)
        except CoreUser.DoesNotExist:
            return Response({"message":"user does not exist"}, status=404)

        is_authenticated = authenticate(email=email, password=password)
                
        if not is_authenticated:
            return Response({"message":"invalid credentials"}, status=406)

        serializer = UserSerializer(user)

        return Response(serializer.data, status=200)




