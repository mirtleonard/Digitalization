from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import parser_classes
from activityReport.models import ActivityReport
from rest_framework.response import Response
from activityReport.views import savePhotos
from api.activityReport.serializers import *
from rest_framework import viewsets
from collections import namedtuple
from rest_framework import status
from django.core.files import File
import json

class ActivityReportViewSet(viewsets.ModelViewSet):
    queryset = ActivityReport.objects.all();
    serializer_class = ActivityReportSerializer
