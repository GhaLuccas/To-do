from django.shortcuts import render , redirect , get_object_or_404
from .models import Task
from . forms import TaskForm


# Create your views here.

tasklist_page = "task:task"

def home_page(request):
    return render(request , 'home.html')

def task_page(request):
    request_user = request.user
    tasks = Task.objects.filter(author=request_user)
    return render (request , "task.html" , {'tasks':tasks})


def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.author = request.user
            task.save()
            return redirect(tasklist_page)
    else:
        form = TaskForm()
        return render(request , 'create_task.html' , {'form':form})

def task_update(request , task_id):
    task = get_object_or_404(Task , id=task_id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect(tasklist_page)
    else:
            form = TaskForm(instance=task)
            return render(request , 'task_update.html' , {'form':form})

def task_read(request , task_id):
    task = get_object_or_404(Task , id=task_id)
    return render(request, 'read_task.html' , {'task':task})

def task_delete(request , task_id):
    task = get_object_or_404(Task , id=task_id)
    task.delete()
    return redirect(tasklist_page)