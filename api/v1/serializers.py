from rest_framework import serializers


class StringListSerializer(serializers.Serializer):
    string_list = serializers.CharField(max_length=1000)
