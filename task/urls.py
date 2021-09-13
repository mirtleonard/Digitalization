from django.urls import path
from task import views

urlpatterns = [
    path('createTask', views.createTask, name = 'createTask'),
    path('updateTask/<int:task_id>', views.updateTask, name = 'updateTask')
]
