from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
import json
from .models import Todo
# Create your views here.

# get all tasks or add task
def get_tasks(request: HttpRequest) -> JsonResponse:
    if request.method == 'GET':
        todos = Todo.objects.all()
        data = []

        response = {
            'todos': data
        }
        for todo in todos:
            data.append(
                {
                    'task': todo.task,
                    'description': todo.description,
                    'completed': todo.completed
                }
            ) 
        return JsonResponse(response)
    else:
        decoded = request.body.decode()
        data = json.loads(decoded)

        todo = Todo()
        todo.task = data.get('task')
        todo.description = data.get('description')
        todo.completed = data.get('completed')

        todo.save()

        new = {
                'task': todo.task,
                'description': todo.description,
                'completed': todo.completed
        }
        return JsonResponse(new)
    
# get task or update task
def get_task(request: HttpRequest, pk) -> JsonResponse:
    if request.method == 'GET':
        try:
            todo = Todo.objects.get(id = pk)
        except:
            return JsonResponse({"result": "This task didn't find"})
        response = {
                    'task': todo.task,
                    'description': todo.description,
                    'completed': todo.completed
        }
        return JsonResponse(response)
    else:
        decoded = request.body.decode()
        data = json.loads(decoded)

        try:
            todo = Todo.objects.get(id = pk)
        except:
            return JsonResponse({"result": "This task didn't find"})
        if data.get('task') != None:
            todo.task = data.get('task')
        if data.get('description') != None:
            todo.description = data.get('description')
        if data.get('completed') != None:
            todo.completed = data.get('completed')

        todo.save()
        updated = {
                    'task': todo.task,
                    'description': todo.description,
                    'completed': todo.completed
        }
        return JsonResponse(updated)
    
# Mark a task as complete
def complete_task(request:HttpRequest, pk):
    if request.method == 'GET':
        try:
            todo = Todo.objects.get(id = pk)
        except:
            return JsonResponse({"result": "This task didn't find"})
        todo.completed = True
        todo.save()
    return JsonResponse({'Updated': True})

# Delete a task
def delete_task(request:HttpRequest, pk):
    if request.method == 'GET':
        try:
            todo = Todo.objects.get(id = pk)
        except:
            return JsonResponse({"result": "This task didn't find"})
        todo.delete()
    return JsonResponse({"Deleted": True})

# Get all completed tasks
def completed_tasks(request: HttpRequest):
    todos = Todo.objects.filter(completed=True)
    data = []

    response = {
        'todos': data
    }
    for todo in todos:
        data.append(
            {
                'task': todo.task,
                'description': todo.description,
                'completed': todo.completed
            }
        ) 
    return JsonResponse(response)

# Get all incompleted tasks
def incompleted_tasks(request: HttpRequest):
    todos = Todo.objects.filter(completed=False)
    data = []

    response = {
        'todos': data
    }
    for todo in todos:
        data.append(
            {
                'task': todo.task,
                'description': todo.description,
                'completed': todo.completed
            }
        ) 
    return JsonResponse(response)