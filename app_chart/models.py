from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self, *args, **kwargs):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=30)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    population = models.PositiveIntegerField()

    def __str__(self, *args, **kwargs):
        return f'{self.name}- {self.country}'
