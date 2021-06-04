from django.urls import path
from . import views

urlpatterns = [
    path('reports/<int:report_id>/edit', views.editReport, name='editReport'),
    path('reports/<int:report_id>', views.viewReport, name= 'viewReport'),
    path('searchReport', views.searchReport, name = 'searchReport'),
    path('addReport', views.addReport, name = 'addReport'),
    path('submitReport', views.submitReport, name = 'submitReport'),
    path('submitReport1', views.submitReport1, name = 'submitReport1'),
]
