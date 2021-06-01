from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login_user', views.login_user, name='login_user'),
    path('profile', views.profile, name='profile'),
]
