from django.db import models 
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.

class Task(models.Model):
    
    STATUS_CHOICES = [
        ('pending' , 'Pending') ,
        ('done' , 'Done') ,
        ('expired' , "Expired")
    ]
    
    title = models.CharField(max_length=30)
    context = models.TextField(max_length=120)
    author = models.ForeignKey(User , on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True) 
    deadline = models.DateTimeField(blank=True, null=True)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='pending',
    )
    
    def __str__(self):
        return self.title
    
    def update_status(self):
        if self.status == 'done':
            return 
        if self.deadline and now() > self.deadline:
            self.status = 'expired'
        else:
            self.status = 'pending'
        self.save()