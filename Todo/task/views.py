from django.shortcuts import render , redirect , get_object_or_404
from .models import Task
from . forms import TaskForm

# Create your views here.

def home_page(request):
    return render(request , 'home.html')

def task_page(request):
    request_user = request.user
    tasks = Task.objects.filter(author=request_user)
    return render (request , "task.html" , {'tasks':tasks})


def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.author = request.user
            task.save()
            return redirect('task:task')
    else:
        form = TaskForm()
        return render(request , 'create_task.html' , {'form':form})
    

def task_read(request , task_id):
    task = get_object_or_404(Task , id=task_id)
    return render(request, 'task:task' , {'task':task})