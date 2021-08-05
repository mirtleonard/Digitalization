from rest_framework import serializers
from drf_base64.fields import Base64FileField
from activityReport.models import ActivityReport

class ActivityReportSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = ActivityReport
        fields = '__all__'
