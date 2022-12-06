from django.contrib import admin
from .models import Garage


@admin.register(Garage)
class GarageAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'level', 'company', 'city']
