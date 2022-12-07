from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main_page'),
    path('signup', views.signup, name='signup_page'),
]
