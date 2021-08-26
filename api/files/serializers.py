from rest_framework import serializers
from eventReport.views import saveEventPhotos
from drf_base64.fields import Base64FileField
from activityReport.views import saveActivityPhotos

class fileSerializer(serializers.Serializer):
    files =  serializers.ListField(child = Base64FileField(required = False))
    id = serializers.IntegerField()
    type = serializers.CharField()

    def create(self, validated_data):
        if (validated_data['type'] == 'activity'):
            saveActivityPhotos(validated_data['files'], validated_data['id'])
        else:
            saveEventPhotos(validated_data['files'], validated_data['id'])
        return validated_data
