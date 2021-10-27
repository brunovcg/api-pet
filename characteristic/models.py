from django.db import models


class Characteristic(models.Model):
    name = models.CharField(max_length=255)