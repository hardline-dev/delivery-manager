from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from user.models import User


class SignupForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = (
            'first_name', 
            'last_name', 
            'username', 
            'email', 
            'password1', 
            'password2'
        )
