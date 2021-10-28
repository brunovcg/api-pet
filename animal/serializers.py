from rest_framework import serializers


class AnimalSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    age = serializers.FloatField()
    weight = serializers.FloatField()
    sex = serializers.CharField()
    group = serializers.IntegerField()

class AnimalCharacteristicSerializer(serializers.Serializer):
    animal_id = serializers.IntegerField()
    characteristic_id = serializers.IntegerField()