from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from activityReport.filters import ActivityReportFilter
from django.shortcuts import render, get_object_or_404
from activityReport.forms import ActivityReportForm
from activityReport.models import ActivityReport
from django.contrib import messages
from task.forms import TaskForm
from django.urls import reverse

# Create your views here.
@login_required
def createTask(request):
    form = TaskForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('profile')
    else :
        context = {'form' : form}
        return render(request, 'createTask.html', context)
