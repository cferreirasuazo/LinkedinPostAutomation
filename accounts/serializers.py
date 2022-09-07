from rest_framework import serializers
from posts.models import Post
from django.contrib.auth.models import User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'id', "first_name", "last_name")

    def create(self, data):
        user = User.objects.create_user(**data)
        return user