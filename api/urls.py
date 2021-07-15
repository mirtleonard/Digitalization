from django.urls import path, include

urlpatterns = [
    path('user/', include('api.user.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('activityReport/', include('api.activityReport.urls')),
]
