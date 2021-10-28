from rest_framework import serializers
from group.serializers import GroupSerializer
from characteristic.serializers import CharacteristicSerializer


class AnimalSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    age = serializers.FloatField()
    weight = serializers.FloatField()
    sex = serializers.CharField()
    group = GroupSerializer()
    characteristics = CharacteristicSerializer(many=True)

# class AnimalCharacteristicSerializer(serializers.Serializer):
#     animal_id = serializers.IntegerField()
#     characteristic_id = serializers.IntegerField()