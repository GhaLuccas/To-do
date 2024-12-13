from django.test import TestCase , Client
from django.urls import reverse
from django.contrib.auth.models import User
from task import views
from task.models import Task
from rest_framework import status

class TestUrl(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_superuser(username='testuser',password='test123')
        self.client = Client()
        self.valid_data = {'title':"hello" , 'context':"word"}
        self.home_url = reverse('task:home')
        self.task_url = reverse('task:task')

        
    def test_home_url(self):
        home_response = self.client.get(self.home_url)
        self.assertEqual(home_response.status_code , status.HTTP_200_OK)
        self.assertTemplateUsed(home_response , 'home.html')
    
    def test_task_url(self):
        self.client.login(username='testuser' , password='test123')
        task_response = self.client.get(self.task_url)
        self.assertEqual(task_response.status_code ,status.HTTP_200_OK )
        self.assertTemplateUsed(task_response , 'task.html')
    
    def test_task_create(self):
        self.client.login(username='testuser' , password='test123')



