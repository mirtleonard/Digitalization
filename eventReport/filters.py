from django.db import models
import django_filters as filters
from eventReport.models import EventReport

class EventReportFilter(filters.FilterSet):
    title = filters.CharFilter(label = 'Titlu', lookup_expr= 'unaccent__icontains')
    center = filters.CharFilter(label = 'Centru', lookup_expr= 'unaccent__icontains')
    username = filters.CharFilter(label = 'Autor', lookup_expr= 'unaccent__icontains')
    class Meta:
        model = EventReport
        fields = ['title', 'center', 'username']
