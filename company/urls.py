from django.urls import path
from . import views

urlpatterns = [
    path('create', views.company_create, name='company_create'),
]
