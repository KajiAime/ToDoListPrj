from django.urls import path
from .views import TodoItemList, TodoItemDetail #, RegisterAPIView

urlpatterns = [
    # path('register/', RegisterAPIView.as_view(), name='register'),
    path('todos/', TodoItemList.as_view(), name='list'),
    path('todos/<int:pk>/', TodoItemDetail.as_view(), name='detail'),
]