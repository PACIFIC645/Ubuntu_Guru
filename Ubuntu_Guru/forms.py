# form.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    # Additional fields can be added here

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)