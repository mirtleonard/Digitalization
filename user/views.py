from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render
from user.forms import registerForm
from django.urls import reverse
from report.models import Report
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
                password = form.cleaned_data.get('password'),
                branch = form.cleaned_data.get('branch'),
                birth = form.cleaned_data.get('birth'),
            )
            user.save()
            return HttpResponseRedirect('profile')
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
    return HttpResponseRedirect(reverse('index'))

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def profile(request):
    user = request.user
    reports = Report.objects.filter(username = request.user.get_username()).order_by('-date')
    return render(request, 'profile.html', {'user' : user, 'reports' : reports})
