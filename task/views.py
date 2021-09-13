from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from activityReport.filters import ActivityReportFilter
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from task.forms import TaskForm
from django.urls import reverse
from task.mail import sendMail
from task.models import Task

# Create your views here.
@login_required
def createTask(request):
    form = TaskForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('profile')
    context = {'form' : form}
    return render(request, 'createTask.html', context)

@login_required
def updateTask(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        task.state = (not task.state)
        task.save()
        return HttpResponseRedirect(reverse('profile'))
    else:
        return render(request, 'editTask.html', {'task' : task})
