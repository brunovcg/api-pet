from django.db import models

class Animal(models.Model):
    name = models.CharField(max_length=255)
    age = models.FloatField()
    weight = models.FloatField()
    sex = models.CharField(max_length=255)
    group = models.ForeignKey('group.Group', on_delete=models.CASCADE, related_name='animal' )
    characteristics = models.ManyToManyField('characteristic.Characteristic', related_name='animal')
    