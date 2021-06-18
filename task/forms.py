from django.forms import *
from task.models import Task

class TaskForm(ModelForm):
    class Meta:
        model = Task
        exclude = ['state']
        widgets = {
            'dueDate' : DateInput(attrs={'type' : 'date'})
        }
