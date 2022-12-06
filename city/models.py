from django.db import models


class City(models.Model):
    name = models.CharField(('name'), max_length=24, unique=True)

    class Meta:
        verbose_name = 'city'
        verbose_name_plural = 'cities'

    def __str__(self):
        return f'{self.name}'


class Distance(models.Model):
    sender = models.OneToOneField(City, on_delete=models.CASCADE, related_name='sender')
    receiver = models.OneToOneField(City, on_delete=models.CASCADE, related_name='receiver')
    distance = models.IntegerField(('distance'))

    class Meta:
        verbose_name = 'distance'
        verbose_name_plural = 'distances'

    def __str__(self):
        return f'{self.sender} - {self.receiver}'
        