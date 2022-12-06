from django.db import models
from company.models import Company
from city.models import City


class Garage(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    level = models.IntegerField(('level'), default=1)

    def __str__(self):
        return f'Garage {self.id}'
