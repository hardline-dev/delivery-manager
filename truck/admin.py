from django.contrib import admin
from .models import Truck, TruckModel


@admin.register(TruckModel)
class TruckModelAdmin(admin.ModelAdmin):
    list_display = ['model']


@admin.register(Truck)
class TruckAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'garage', 'driver', 'model', 'mileage']
