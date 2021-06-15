from django.urls import path
from . import views

urlpatterns = [
    path('updateEventReport/<int:report_id>', views.updateEventReport, name = 'updateEventReport'),
    path('deleteEventReport/<int:report_id>', views.deleteEventReport, name = 'deleteEventReport'),
    path('eventReport/<int:report_id>', views.viewEventReport, name= 'viewEventReport'),
    path('searchEventReports', views.searchEventReports, name = 'searchEventReports'),
    path('createEventReport', views.createEventReport, name = 'createEventReport'),
]
