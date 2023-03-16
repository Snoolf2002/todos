from django.urls import path, include
from .views import get_task, get_tasks, complete_task, completed_tasks, incompleted_tasks, delete_task
urlpatterns = [
    path('tasks/', get_tasks),
    path('tasks/<int:pk>', get_task),
    path('tasks/<int:pk>/complete', complete_task),
    path('tasks/<int:pk>/delete', delete_task),
    path('tasks/completed', completed_tasks),
    path('tasks/incompleted', incompleted_tasks),

]