from django.forms import *
from django.db import models
import django_filters as filters
from activityReport.models import ActivityReport

class ActivityReportFilter(filters.FilterSet):
    branch = filters.CharFilter(label = 'Ramură', lookup_expr= 'unaccent__icontains',
        widget = Select(choices = (
                ('', ''),
                ('Lupișori', 'Lupișori'),
                ('Temerari', 'Temerari'),
                ('Exploratori', 'Exploratori'),
                ('Seniori', 'Seniori'),
        )))
    areas = filters.CharFilter(label = 'Arie de dezvoltare', lookup_expr= 'unaccent__icontains',
        widget = Select(choices = (
                ('', ''),
                ('intelectuală', 'intelectuală'),
                ('spirituală', 'spirituală'),
                ('caracter', 'caracter'),
                ('afectivă', 'afectivă'),
                ('socială', 'socială'),
                ('fizică', 'fizică'),
        )))
    title = filters.CharFilter(label = 'Titlu', lookup_expr= 'unaccent__icontains')
    username = filters.CharFilter(label = 'Autor', lookup_expr= 'unaccent__icontains')
    location = filters.CharFilter(label = 'Locație', lookup_expr= 'unaccent__icontains')
    class Meta:
        model = ActivityReport
        fields = ['title', 'username', 'location', 'branch', 'areas']
