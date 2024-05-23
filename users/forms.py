from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from .models import CustomUser

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        {'placeholder': 'Username',
         'class': 'form_username'}
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        {'placeholder': 'Password',
         'class': 'form_password'}
    }))
    
class SignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        {'placeholder': 'Username',
         'class': 'form_username'}
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Email',
        'class': 'form_email'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        {'placeholder': 'Password',
         'class': 'form_password'}
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        {'placeholder': 'Password',
         'class': 'form_password'}
    }))