from django.contrib import admin
from .models import City, Distance


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    ordering = ('id',)


@admin.register(Distance)
class DistanceAdmin(admin.ModelAdmin):
    list_display = ['id', 'sender', 'receiver', 'distance']
    ordering = ('id',)
