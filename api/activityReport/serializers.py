from rest_framework import serializers
from activityReport.models import ActivityReport

class ActivityReportSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    date = serializers.DateTimeField(required = False)

    class Meta:
        model = ActivityReport
        fields = '__all__'
