import django_filters
from django.forms import *
from django.db import models
from activityReport.models import ActivityReport

class ActivityReportFilter(django_filters.FilterSet):
    areas = django_filters.CharFilter(widget = Select(choices = (
                ('intelectuala', 'intelectuala'),
                ('spirituala', 'spirituala'),
                ('caracter', 'caracter'),
                ('afectiva', 'afectiva'),
                ('sociala', 'sociala'),
                ('fizica', 'fizica'))))
    class Meta:
        model = ActivityReport
        fields = ['title', 'username', 'location']
        filter_overrides = {
            models.CharField: {
                'filter_class' : django_filters.CharFilter,
                'extra' : lambda f: {
                    'lookup_expr': 'unaccent__icontains',
                }
            }
        }
        widgets = {
            'areas' : Select(choices = (
                ('intelectuala', 'intelectuala'),
                ('spirituala', 'spirituala'),
                ('caracter', 'caracter'),
                ('afectiva', 'afectiva'),
                ('sociala', 'sociala'),
                ('fizica', 'fizica'))),
        }
    def __init__(self, request, branch, *args, **kwargs):
        super().__init__(request, *args, **kwargs)
        self.branch = branch
        self.filters['areas'].label = "Arie de dezvoltare"
        self.filters['title'].label = "Titlu"
        self.filters['username'].label = "Autor"
        self.filters['location'].label = "Locație"

    def qs(self):
        parent = super().qs
        return parent.filter(branch__icontains = self.branch)
