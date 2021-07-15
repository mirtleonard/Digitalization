from activityReport.models import ActivityReport
from api.activityReport.serializers import *
from rest_framework import viewsets

class ActivityReportsViewSet(viewsets.ModelViewSet):
    queryset = ActivityReport.objects.all();
    serializer_class = ActivityReportSerializer
