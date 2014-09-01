from django.db import models


class Car(models.Model):
    name = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
