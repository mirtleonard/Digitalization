from rest_framework import serializers
from activityReport.models import EventReport

class ActivityReportSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EventReport
        fields = '__all__'
