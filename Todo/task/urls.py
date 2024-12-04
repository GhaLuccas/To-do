from django.urls import path
from .views import home_page , task_page , create_task

app_name = 'task'

urlpatterns =[
    path("home/" , home_page , name='home'),
    path('task/' , task_page , name='task') ,
    path('task/create' , create_task , name='create-task' )
]