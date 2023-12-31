from django.urls import path
from .views import TodoView, TodoViewDetail

urlpatterns = [
    path('tasks/', TodoView.as_view(), name='tasks'),
    path('tasks/<int:pk>', TodoViewDetail.as_view(), name='tasks_detail')
]