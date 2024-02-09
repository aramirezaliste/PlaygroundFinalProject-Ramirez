from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class CustomAuthenticationForm(AuthenticationForm):
   
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            "username": forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder':'Nombre de usuario',
                    }
                ),
            'password': forms.PasswordInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder':'Contraseña'
                       }
                ),
        }
        
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(
                attrs = {
                    "class": "form-control"
                    }
                ),
            'password1': forms.PasswordInput(
                attrs = {
                    'class': 'form-control'
                    }
                ),
            'password2': forms.PasswordInput(
                attrs = {
                    'class': 'form-control'
                    }
                ),
        }
        labels = {
            'username': 'Nombre de usuario',
            'password1': 'Contraseña',
            'password2': 'Confirmar contraseña'
        }


