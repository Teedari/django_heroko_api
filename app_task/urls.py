from django.urls import path
from .views import TodoDetailApi, TodoListApi




urlpatterns = [
  path('', TodoListApi.as_view()),
  # path('/<int:pk>', TodoDetailApi.as_view()),
]