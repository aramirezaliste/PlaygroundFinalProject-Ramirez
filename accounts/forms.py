from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(help_text='', label='', widget=forms.TextInput(
                attrs = {
                    'class': "form-control",
                    'placeholder': 'Nombre de usuario'
                    }
                ) )
    password = forms.CharField(help_text='', label='', widget=forms.PasswordInput(
                attrs = {
                    'class': "form-control",
                    'placeholder': 'Contraseña'
                    }
                ) )
   
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {}
        
        
class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(help_text='', label='', widget=forms.TextInput(
                attrs = {
                    'class': "form-control",
                    'placeholder': 'Nombre de usuario'
                    }
                ) )
    email = forms.EmailField(help_text='', label='', widget=forms.EmailInput(
                attrs = {
                    'class': "form-control",
                    'placeholder': 'Email'
                    }
                ) )
    password1 = forms.CharField(help_text='', label='', widget=forms.PasswordInput(
                attrs = {
                    'class': "form-control",
                    'placeholder': 'Contraseña'
                    }
                ) )
    password2 = forms.CharField(help_text='', label='', widget=forms.PasswordInput(
                attrs = {
                    'class': "form-control",
                    'placeholder': 'Confirmar Contraseña'
                    }
                ) )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {}
    


