from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from user.models import User


# Create your views here.

def index(request):
    return render(request, 'login.html')

def register(request):
    if (request.POST.get('password1') and request.POST.get('password1') != request.POST.get('password2')):
        raise ValueError("password don't match")
    user = User(
    username = request.POST.get('username'),
    email = request.POST.get('email'),
    branch = request.POST.get('branch'),
    birth = request.POST.get('birth'),
    )
    user.set_password(request.POST.get('password1')),
    user.save()
    return HttpResponseRedirect(reverse('index'))

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
