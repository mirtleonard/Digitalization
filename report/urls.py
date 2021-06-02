from django.urls import path
from . import views

urlpatterns = [
    path('viewReports', views.viewReports, name = 'viewReports'),
    path('searchReport', views.searchReport, name = 'searchReport'),
    path('addReport', views.addReport, name = 'addReport'),
    path('submitReport', views.submitReport, name = 'submitReport'),
]
