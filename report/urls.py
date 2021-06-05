from django.urls import path
from . import views

urlpatterns = [
    path('reports/<int:report_id>/updateReport', views.updateReport, name = 'updateReport'),
    path('reports/<int:report_id>', views.viewReport, name= 'viewReport'),
    path('searchReport', views.searchReport, name = 'searchReport'),
    path('createReport', views.createReport, name = 'createReport'),
]
