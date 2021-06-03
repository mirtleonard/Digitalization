from django.urls import path
from . import views

urlpatterns = [
    path('reports/<int:report_id>', views.viewReport, name = 'viewReport'),
    path('searchReport', views.searchReport, name = 'searchReport'),
    path('addReport', views.addReport, name = 'addReport'),
    path('submitReport', views.submitReport, name = 'submitReport'),
]
