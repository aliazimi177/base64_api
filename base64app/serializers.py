from rest_framework import serializers 


class Base64Serializer(serializers.Serializer):
    text = serializers.CharField(required=False)
    base64 = serializers.CharField(required=False)
