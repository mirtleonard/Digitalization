from rest_framework import serializers
from activityReport.models import ActivityReport

class ActivityReportSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ActivityReport
        fields = '__all__'
