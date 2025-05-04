from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class SignupForm(UserCreationForm):
    full_name = forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your full name...'}))
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email address...'}))
    username = forms.CharField(label="", max_length=20, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username...'}))
    password1 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password', 'type': 'password', 'placeholder': 'Enter your password...'}))
    password2 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password', 'type': 'password', 'placeholder': 'Enter your password again...'}))
    
    class Meta:
        model = User
        fields = ('full_name', 'email', 'username', 'password1', 'password2')