from django.urls import path
from . import views

urlpatterns = [
    path('reports/<int:report_id>/updateActivityReport', views.updateActivityReport, name = 'updateActivityReport'),
    path('reports/<int:report_id>/deleteReport', views.deleteReport, name = 'deleteReport'),
    path('createActivityReport', views.createActivityReport, name = 'createActivityReport'),
    path('createEventReport', views.createEventReport, name = 'createEventReport'),
    path('reports/<int:report_id>', views.viewReport, name= 'viewReport'),
    path('searchReport/<str:type>', views.searchReport, name = 'searchReport'),
]
