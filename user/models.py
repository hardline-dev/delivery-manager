from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(('username'), max_length=24, unique=True)
    experience = models.IntegerField(('experience'), default=0)
    rating = models.FloatField(('rating'), default=0.0)

    def full_name(self):
        return f'{self.first_name} {self.last_name}'
