from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
from django.http import JsonResponse
from .models import Task
from . forms import TaskForm


# Create your views here.

tasklist_page = "task:task"


def home_page(request):
    return render(request , 'home.html')

    

@login_required
def task_page(request):
    
    request_user = request.user
    tasks = Task.objects.filter(author=request_user)
    
    for task in tasks:
        task.update_status()
    
    search_query = request.GET.get('search', '') 
    completed = request.GET.get('completed' , '')
    pending = request.GET.get('pending' , '')
    expired = request.GET.get('expired' , '')
    
    if search_query:
        tasks = tasks.filter(Q(title__icontains=search_query) | Q(context__icontains=search_query))
    if completed.lower() == "true":
        tasks = tasks.filter(status='done')
    if pending.lower() == "true":
        tasks = tasks.filter(status='pending')
    if expired.lower() =="true":
        tasks = tasks.filter(status='expired')
    
    return render (request , "task.html" , {'tasks':tasks})

@login_required
def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.author = request.user
            task.save()
            messages.success(request, 'Task created successfully!')
            return redirect(tasklist_page)
    else:
        form = TaskForm()
    return render(request , 'create_task.html' , {'form':form})

@login_required
def task_update(request , task_id):
    task = get_object_or_404(Task , id=task_id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task created successfully!')
            return redirect(tasklist_page)
    else:
        form = TaskForm(instance=task)
    return render(request , 'task_update.html' , {'form':form})

@login_required
def task_read(request , task_id):
    task = get_object_or_404(Task , id=task_id)
    return render(request, 'read_task.html' , {'task':task})

@login_required
def task_delete(request , task_id):
    task = get_object_or_404(Task , id=task_id)
    task.delete()
    return redirect(tasklist_page)


@login_required
def toggle_status(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(Task, id=task_id)
        
        # Atualiza status baseado no deadline
        task.update_status()
        
        if task.status == 'done':
            task.status = 'pending'
        elif task.status in ['pending', 'expired']:
            task.status = 'done'
        
        task.save()
        return JsonResponse({'success': True, 'status': task.status})
    
    return JsonResponse({'success': False, 'message': 'Task not found or invalid request'})
