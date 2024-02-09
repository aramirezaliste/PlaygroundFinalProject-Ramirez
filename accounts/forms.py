from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
#from django.contrib.auth.models import User
from .models import CustomUser

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
        model = CustomUser
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
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {}
    

class UserModificationForm(forms.ModelForm):
            first_name = forms.CharField(help_text='', label='', widget=forms.TextInput(
                    attrs = {
                        'class': "form-control",
                        'placeholder': 'Nombre'
                        }
                    ) )
            last_name = forms.CharField(help_text='', label='', widget=forms.TextInput(
                    attrs = {
                        'class': "form-control",
                        'placeholder': 'Apellido'
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
                            'placeholder': 'Confirmar contraseña'
                            }
                        ) )
            link = forms.CharField(help_text='', label='', widget=forms.TextInput(
                        attrs = {
                            'class': "form-control",
                            'placeholder': 'Link a pagina'
                            }
                        ) )
            description = forms.CharField(help_text='', label='', widget=forms.Textarea(
                        attrs = {
                            'rows': 3,
                            'class': "form-control",
                            'placeholder': 'Descripcion'
                            }
                        ) )
            class Meta:
                model = CustomUser
                fields = ['first_name', 'last_name', 'email', 'password1', 'password2', 'link', 'description']
