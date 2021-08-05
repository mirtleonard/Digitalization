from rest_framework import serializers
from activityReport.views import savePhotos
from eventReport.views import save_photos
from drf_base64.fields import Base64FileField

class fileSerializer(serializers.Serializer):
    files =  serializers.ListField(child = Base64FileField(required = False))

    def create(self, validated_data):
        print(validated_data, 'aha')
        savePhotos(validated_data['files'], 0)
        return validated_data
