from django import forms
from .models import task_detail

class TaskDetailForm(forms.ModelForm):
    class Meta:
        model = task_detail
        fields = ['task_name','status']
    