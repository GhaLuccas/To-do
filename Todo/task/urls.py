from django.urls import path
from .views import home_page

app_name = 'task'

urlpatterns =[
    path("home/" , home_page , name='home'),
]