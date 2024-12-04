from django.shortcuts import render , redirect
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views import generic , View  
from django.views.generic import CreateView , TemplateView
from django.views.generic.edit import FormView
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
        