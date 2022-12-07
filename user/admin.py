from django.contrib import admin
from django.contrib.auth.models import Group
from .models import User


admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'full_name', 'company']
    fieldsets = (
        (None, {'fields': (
            'username', 'password'
        )}),
        ('Player info', {'fields': (
            'first_name', 'last_name', 'email'
        )}),
        ('Game info', {'fields': (
            'experience', 'rating'
        )}),
        ('Permissions', {'fields': (
            'is_staff', 'is_superuser'
        )}),
    )
