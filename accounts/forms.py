from cProfile import label

from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control' , 'placeholder': 'Enter username'}),
            'email': forms.TextInput(attrs={'class': 'form-control' , 'placeholder': 'Enter email'}),
            }