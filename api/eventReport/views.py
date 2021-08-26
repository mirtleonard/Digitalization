from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from eventReport.models import EventReport
from api.eventReport.serializers import *
from rest_framework import viewsets
from rest_framework import status
from django.conf import settings
import os, shutil, zipfile

class EventReportSerializers(viewsets.ModelViewSet):
    parser_classes = [JSONParser]
    queryset = EventReport.objects.all();
    serializer_class = EventReportSerializers

    def destroy(self, request, *args, **kwargs):
        report = self.get_object()
        try:
            shutil.rmtree(settings.MEDIA_ROOT + '/eventReport/' + str(report.id))
        except OSError as e:
            pass
        report.delete()
        return Response(status = status.HTTP_201_CREATED)
