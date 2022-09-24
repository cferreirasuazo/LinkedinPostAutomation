from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import PostViewSet, CancelScheduleTask, PublishPost,UserPosts
from accounts.views import UserSignUpView, UserSignInView

router = DefaultRouter()
router.register("posts", PostViewSet, "post")

urlpatterns = [
    path ('', include(router.urls)),
    path("task/<id>/delete", view=CancelScheduleTask.as_view(), name="cancel-schedule-task"),
    path("posts/<id>/publish", view=PublishPost.as_view(), name="publish-post"),
    path('users/signup', view=UserSignUpView.as_view(), name='signup-user'),
    path('users/signin', view=UserSignInView.as_view(), name='signin-user'),
    path('users/<user_id>/posts', view=UserPosts.as_view(), name="user-posts"),
]