from rest_framework import serializers

class CharacteristicSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()