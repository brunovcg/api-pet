from django.db import models

class Animal(models.Model):
    name = models.CharField(max_length=255)
    age = models.FloatField()
    weigth = models.FloatField()
    sex = models.CharField(max_length=255)
    group = models.ForeignKey('group.Group', on_delete=models.CASCADE, related_name='animal' )
    characteristics = models.ManyToManyField('characteristic.Characteristic', related_name='animal', through='animal.AnimalCharacteristic')


class AnimalCharacteristic(models.Model):
    animal_id = models.ForeignKey('animal.Animal', on_delete=models.CASCADE)
    characteristic_id = models.ForeignKey('characteristic.Characteristic', on_delete=models.CASCADE)