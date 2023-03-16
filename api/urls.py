from django.urls import path, include
from .views import get_task, get_tasks, complete, completed_tasks, incompleted_tasks, delete
urlpatterns = [
    path('tasks/', get_tasks),
    path('tasks/<int:pk>', get_task),
    path('tasks/<int:pk>/complete', complete),
    path('tasks/<int:pk>/delete', delete),
    path('tasks/completed', completed_tasks),
    path('tasks/incompleted', incompleted_tasks),

]