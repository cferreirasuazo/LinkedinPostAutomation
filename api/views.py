from csv import excel
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import UpdateAPIView
from posts.models import Post
from .serializer import PostSerializer
from posts.utils.Exceptions import NotValidScheduleDate
from posts.tasks import linkedin_post
from postautomation.celery import app


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class CancelScheduleTask(UpdateAPIView):
    def patch(self, request,id):
        try:
            post = Post.objects.get(id=id)
            app.control.revoke(post.task_id, terminate=True)
            post.task_id = "__update__"
            post.to_publish = False
            post.save()
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
            linkedin_post.apply_async(args=(id,), countdown=240 )
            post.save()
            serializer = PostSerializer(post)
        except Exception: 
            return Response({"message": "Error"}, status=500)
        except NotValidScheduleDate:
            return Response({"message": "Invalid schedule date"}, status=500)
        except Post.DoesNotExist:
            return Response({"message":"Post not found"}, status=404)

        return Response(serializer.data, status=200)