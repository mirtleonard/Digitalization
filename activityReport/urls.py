from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('updateActivityReport/<int:report_id>', views.updateActivityReport, name = 'updateActivityReport'),
    path('deleteActivityReport/<int:report_id>', views.deleteActivityReport, name = 'deleteActivityReport'),
    path('activityReport/<int:report_id>', views.viewActivityReport, name= 'viewActivityReport'),
    path('searchActivityReports/<str:branch>', views.searchActivityReports, name = 'searchActivityReports'),
    path('createActivityReport', views.createActivityReport, name = 'createActivityReport'),
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
