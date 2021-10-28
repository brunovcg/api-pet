from rest_framework import serializers


class GroupSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    scientific_name = serializers.CharField()