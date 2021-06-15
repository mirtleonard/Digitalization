import django_filter
from report.models import EventReport, ActivityReport

class EventReportFilter(django_filter.FilterSet):
    class Meta:
        model = EventReport
        fields = '__all__'


class ActivityReportFilter(django_filter.FilterSet):
    class Meta:
        model = ActivityReport
        fields = '__all__'
