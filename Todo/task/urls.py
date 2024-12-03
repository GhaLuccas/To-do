from django.urls import path
from .views import home_page , task_page , TaskCreateView

app_name = 'task'

urlpatterns =[
    path("home/" , home_page , name='home'),
    path('task/' , task_page.as_view() , name='task') ,
    path('task/create' , TaskCreateView.as_view() , name='create-task' )
]