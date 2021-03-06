from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from activityReport.models import ActivityReport
from eventReport.models import EventReport
from django.contrib import messages
from django.shortcuts import render
from user.forms import registerForm
from django.urls import reverse
from task.models import Task
from user.models import User


# Create your views here.

def index(request):
    if (request.user.username != ""):
        return HttpResponseRedirect('profile')
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        form = registerForm(request.POST)
        if (form.is_valid()):
            user = User(
                username = form.cleaned_data.get('username'),
                email = form.cleaned_data.get('email'),
                branch = form.cleaned_data.get('branch'),
                birth = form.cleaned_data.get('birth'),
            )
            user.set_password(form.cleaned_data.get('password'))
            user.save()
            messages.success(request, "Utilizatorul a fost creat.")
            return index(request)
    else:
        form = registerForm()
    return render (request, 'register.html', {'form' : form})

def login_user(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username = username, password = password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('profile'))
    messages.error(request, "Nu există utilizator cu acest nume sau parolă!")
    return HttpResponseRedirect(reverse('index'))

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def profile(request):
    user = request.user
    ActivityReports = ActivityReport.objects.filter(username = request.user.get_username()).order_by('-date')
    EventReports = EventReport.objects.filter(username = request.user.get_username()).order_by('-beginingDate')
    Tasks = Task.objects.filter(user = request.user.id).order_by('-dueDate')
    context = {
        'user' : user,
        'EventReports' : EventReports,
        'ActivityReports' : ActivityReports,
        'Tasks' : Tasks,
    }
    return render(request, 'profile.html', context)
