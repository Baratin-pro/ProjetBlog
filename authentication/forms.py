from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class LoginForms(forms.Form):
    username = forms.CharField(max_length=70, label='Identifiant')
    password = forms.CharField(max_length=70, widget=forms.PasswordInput, label='Mot de passe')
