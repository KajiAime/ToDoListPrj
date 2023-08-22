from rest_framework import generics
from .models import TodoItem
from .serializers import TodoItemSerializer #, UserSerializer
# from rest_framework.authentication import BasicAuthentication
# from rest_framework.permissions import IsAuthenticated, AllowAny

from django.contrib.auth.models import User
# from django.contrib.auth.hashers import make_password

# Create your views here.
class TodoItemList(generics.ListCreateAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
    # Below is for authentication and authorization
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]

class TodoItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer

# class RegisterAPIView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
    # permission_classes = [AllowAny]

    # def create(self, request, *args, **kwargs):
    #     #To hash a password before saving it to a database
    #     request.data['password'] = make_password(request.data['password'])
    #     return super().create(request, *args, **kwargs)
