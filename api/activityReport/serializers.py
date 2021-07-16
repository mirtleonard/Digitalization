from rest_framework import serializers
from activityReport.models import ActivityReport

class ActivityReportSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = ActivityReport
        fields = '__all__'
