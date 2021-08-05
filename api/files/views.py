from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from . import serializers


class FileView(APIView):
    parser_classes = [FormParser, MultiPartParser]

    def post(self, request):
        serializer = serializers.fileSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status = status.HTTP_200_OK)
        print(serializer.errors)
        return Response(status = status.HTTP_400_BAD_REQUEST)
