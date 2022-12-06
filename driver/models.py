from django.db import models


class Driver(models.Model):
    name = models.CharField(('name'), max_length=24, unique=True)
    rating = models.FloatField(('rating'), default=0.0)
    salary = models.FloatField(('salary'), default=0.0)

    def __str__(self):
        return f'{self.name}'
