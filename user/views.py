from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from user.models import User


# Create your views here.

def index(request):
    return render(request, 'login.html')

def login_user(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username = username, password = password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('profile'))
    return HttpResponseRedirect(reverse('index'))

def profile(request):
    return render(request, 'profile.html')
