from rest_framework.decorators import parser_classes
from activityReport.models import ActivityReport
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from api.activityReport.serializers import *
from googleAPI.api import deleteFile
from rest_framework import viewsets
from rest_framework import status
from django.conf import settings

class ActivityReportViewSet(viewsets.ModelViewSet):
    parser_classes = [JSONParser]
    queryset = ActivityReport.objects.all();
    serializer_class = ActivityReportSerializer

    def destroy(self, request, *args, **kwargs):
        report = self.get_object()
        deleteFile('activity' + str(report.id))
        report.delete()
        return Response(status = status.HTTP_201_CREATED)
