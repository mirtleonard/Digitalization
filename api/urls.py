from django.urls import path, include

urlpatterns = [
    path('file/', include('api.files.urls')),
    path('user/', include('api.user.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('eventReport/', include('api.eventReport.urls')),
    path('activityReport/', include('api.activityReport.urls')),
]
