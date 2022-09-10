from django.db import models

# Create your models here.
class task_detail(models.Model):
    task_name = models.CharField(max_length=200)  
    status=models.CharField(max_length = 200, default = "Incomplete Task")

def __str__(self):   
    return self.task_name 

