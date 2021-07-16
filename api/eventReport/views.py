from eventReport.models import EventReport
from api.eventReport.serializers import *
from rest_framework import viewsets

class EventReportSerializers(viewsets.ModelViewSet):
    queryset = EventReport.objects.all();
    serializer_class = EventReportSerializers
