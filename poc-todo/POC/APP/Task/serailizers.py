from .models import UserTasks
from rest_framework import serializers
from APP.Users.models import User


class TaskGetSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserTasks
        fields = ('id', 'description', 'state', 'user_id')


class UserSerializer(serializers.ModelSerializer):
    user = TaskGetSerializer(many=True)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'user')
