from django.db import models
from garage.models import Garage
from driver.models import Driver


class TruckModel(models.Model):
    model = models.CharField(('model'), max_length=40)

    def __str__(self):
        return f'{self.model}'


class Truck(models.Model):
    garage = models.ForeignKey(Garage, on_delete=models.CASCADE)
    driver = models.OneToOneField(Driver, on_delete=models.CASCADE, null=True)
    model = models.OneToOneField(TruckModel, on_delete=models.CASCADE)
    engine = models.IntegerField(('amount of horsepower'))
    tank = models.IntegerField(('tank size'))
    mileage = models.IntegerField(('mileage'), default=0)

    def __str__(self):
        return f'Truck {self.id}'
