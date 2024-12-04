from django.db import models 
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=30)
    context = models.TextField(max_length=80)
    author = models.ForeignKey(User , on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    done = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title