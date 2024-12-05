from django.urls import path
from . import views 

app_name = 'task'

urlpatterns =[
    path("home/" , views.home_page , name='home'),
    path('task/' , views.task_page , name='task'),
    path('task/create/' , views.task_create , name='task-create' ),
    path('task/<int:task_id>/read/', views.task_read , name='task-read'),
    path("task/<int:task_id>/delete/" , views.task_delete , name='task-delete'),
    path('task/<int:task_id>/update/', views.task_update , name='task-update' ),
]