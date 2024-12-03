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

class task_page(TemplateView):
    template_name = 'task.html'



class TaskCreateView(FormView):
    template_name = 'create_task.html'
    form_class = TaskForm
    success_url = '//'
    
    def form_valid(self, form):
        return HttpResponseRedirect(self.get_success_url()) 