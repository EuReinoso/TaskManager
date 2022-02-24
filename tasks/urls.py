from django.urls import path
from . import views

urlpatterns = [
    path('', views.tasks, name='tasks'),
    path('del-task-<int:id>', views.del_task, name='del-task'),
    path('del-block-<int:id>', views.del_block, name='del-block'),
    path('change-task-status-<int:id>', views.change_task_status, name='change-task-status'),
    path('add-task/<int:id>', views.add_task, name='add-task'),
    path('add-user/<int:id>', views.add_user, name='add-user'),
    path('del-user-u=<int:user_id>-b=<int:block_id>', views.del_user, name='del-user'),
]
