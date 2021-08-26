from rest_framework import serializers
from eventReport.models import EventReport

class EventReportSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = EventReport
        fields = '__all__'
