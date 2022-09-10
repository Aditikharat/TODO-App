from ast import Return
from http.client import HTTPResponse
from urllib import request, response
from django.shortcuts import render,get_object_or_404,redirect
from . models import task_detail
from django.http import HttpResponse
from .forms import TaskDetailForm
# Create your views here.
def task_new(request):
    if request.method=='POST':
        form_data=TaskDetailForm(request.POST)
        if form_data.is_valid():
             Post_data=form_data.save()
             return redirect(task_list)

    form_data=TaskDetailForm()
    return render(request,'Taskstatus/index.html',{'form_data':form_data})

def task_list(request):
    data =task_detail.objects.all().order_by('-id')
    return render(request,'Taskstatus/tasklist.html', {'data':data})


def delete_task(request,pk):
    post = get_object_or_404(task_detail,pk=pk)
    post.delete()
    return redirect('task_list')


def update_task(request,pk):
    post = get_object_or_404(task_detail,pk=pk)
    post.status='Task Complete'
    post.save()
    return redirect('task_list')


