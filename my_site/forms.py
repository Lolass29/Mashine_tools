from django.contrib.auth.forms import UserCreationForm
from django import forms

from my_site.models import User


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class':  "text", "placeholder": "Enter your username"}))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class':  "text", "placeholder": "Enter your email"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':  "text", "placeholder": "Enter your password"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':  "text", "placeholder": "Enter your password"}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
