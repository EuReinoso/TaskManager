from django.urls import path
from . import views


urlpatterns = [
    path('', views.tasks, name='tasks'),
    path('delete-task-<int:id>', views.del_task, name='del-task')
]