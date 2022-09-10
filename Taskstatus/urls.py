from django.urls import path

from Taskstatus.models import task_detail
from . import views 
urlpatterns = [

path('',views.task_new,name='task_new'),
path('tasklist',views.task_list,name='task_list'),
path('delete/<int:pk>/',views.delete_task,name='delete_task'),
path('update/<int:pk>/',views.update_task,name='update_task'),

    
]