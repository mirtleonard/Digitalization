from googleAPI.api import saveFiles
from rest_framework import serializers
from drf_base64.fields import Base64FileField

class fileSerializer(serializers.Serializer):
    files =  serializers.ListField(child = Base64FileField(required = False))
    id = serializers.IntegerField()
    type = serializers.CharField()

    def create(self, validated_data):
        saveFiles(validated_data['files'], validated_data['type'] + str(validated_data['id']))
        return validated_data
