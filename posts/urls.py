from . import views
from django.urls import path, include
app_name="posts"

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('forget-password', views.forget_password, name="forget-password")
]


