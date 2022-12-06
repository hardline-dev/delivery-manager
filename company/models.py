from django.db import models
from user.models import User


class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(('name'), max_length=24, unique=True)
    money = models.IntegerField(('money'), default=100000)

    class Meta:
        verbose_name = 'company'
        verbose_name_plural = 'companies'

    def __str__(self):
        return f'{self.name}'
