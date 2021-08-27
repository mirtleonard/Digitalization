from django.forms import *
from django.db import models
import django_filters as filters
from activityReport.models import ActivityReport

class ActjvityReportFilter(django_filters.FilterSet):
    branch = filters.CharFilter(label = 'Ramură', lookup_expr= 'unaccent__icontains',
        widget = Select(choices = (
                ('', ''),
                ('intelectuala', 'intelectuala'),
                ('spirituala', 'spirituala'),
                ('caracter', 'caracter'),
                ('afectiva', 'afectiva'),
                ('sociala', 'sociala'),
                ('fizica', 'fizica'),
        )))
    areas = filters.CharFilter(label = 'Arie de dezvoltare', lookup_expr= 'unaccent__icontains',
        widget = Select(choices = (
                ('', ''),
                ('Lupisori', 'Lupisori'),
                ('Temerari', 'Temerari'),
                ('Exploratori', 'Exploratori'),
                ('Seniori', 'Seniori'),
        )))
    title = filters.CharFilter(label = 'Titlu', lookup_expr= 'unaccent__icontains')
    username = filters.CharFilter(label = 'Autor', lookup_expr= 'unaccent__icontains')
    location = filters.CharFilter(label = 'Autor', lookup_expr= 'unaccent__icontains')
    class Meta:
        model = ActivityReport
        fields = ['title', 'username', 'location', 'branch', 'areas']
