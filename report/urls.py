from django.urls import path
from . import views

urlpatterns = [
    path('updateActivityReport/<int:report_id>', views.updateActivityReport, name = 'updateActivityReport'),
    path('deleteActivityReport/<int:report_id>', views.deleteActivityReport, name = 'deleteActivityReport'),
    path('activityReport/<int:report_id>', views.viewActivityReport, name= 'viewActivityReport'),
    path('createActivityReport', views.createActivityReport, name = 'createActivityReport'),
    path('updateEventReport/<int:report_id>', views.updateEventReport, name = 'updateEventReport'),
    path('deleteEventReport/<int:report_id>', views.deleteEventReport, name = 'deleteEventReport'),
    path('eventReport/<int:report_id>', views.viewEventReport, name= 'viewEventReport'),
    path('createEventReport', views.createEventReport, name = 'createEventReport'),
    path('searchReport/<str:type>', views.searchReport, name = 'searchReport'),
]
