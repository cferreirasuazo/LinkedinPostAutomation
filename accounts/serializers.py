from rest_framework import serializers
from posts.models import Post
from accounts.models import CoreUser



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoreUser
        fields = ('email', 'id', "first_name", "last_name")

    def create(self, data):
        user = CoreUser.objects.create_user(**data)
        return user