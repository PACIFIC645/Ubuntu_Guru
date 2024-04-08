# Ubuntu_Guru/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    """
    Extends the default UserCreationForm to include username, email, and password fields explicitly.
    Used for registering new users from the frontend.
    """
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)
