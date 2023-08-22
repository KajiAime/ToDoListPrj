from rest_framework import serializers
from django.contrib.auth.models import User
from .models import TodoItem

class TodoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = ('id', 'title', 'description', 'completed')

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'password', 'email']
#         extra_kwargs = {'password':{'write_only': True}}