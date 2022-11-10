from django.db import models

# Create your models here.

class basededatos_ok(models.Model):
    nombre = models.CharField(max_length=20)
    edad = models.IntegerField()
    fecha = models.DateField()
    