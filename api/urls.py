from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CancelScheduleTask, PublishPost
from accounts.views import UserSignUpView

router = DefaultRouter()
router.register("posts", PostViewSet, "post")

urlpatterns = [
    path ('', include(router.urls)),
    path("task/<id>/delete", view=CancelScheduleTask.as_view(), name="cancel-schedule-task"),
    path("posts/<id>/publish", view=PublishPost.as_view(), name="publish-post"),
    path('auth/signup', view=UserSignUpView.as_view(), name='signup-user')
]