from django.db import models

# Create your models here.

class Planet(models.Model):
    name = models.CharField(max_length=255)
    population = models.IntegerField()
    terrain = models.CharField(max_length=255)
    climate = models.CharField(max_length=255)

    def __str__(self):
        return self.name