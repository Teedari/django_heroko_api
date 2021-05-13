from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import TodoSerializer
from .models import Todo
# Create your views here.


class TodoListApi(generics.ListCreateAPIView):
  queryset = Todo.objects.all()
  serializer_class = TodoSerializer
  permission_classes = (permissions.AllowAny,)

class TodoDetailApi(generics.RetrieveDestroyAPIView):
  queryset = Todo.objects.all()
  serializer_class = TodoSerializer
  permission_classes = (permissions.AllowAny,)
