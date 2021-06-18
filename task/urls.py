from django.urls import path
from task import views

urlpatterns = [
    path('createTask', views.createTask, name = 'createTask')
]
