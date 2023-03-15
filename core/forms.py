from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from novo_portal_dva.models import Usuario


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'w-full py-4 px-6 rounded-xl',
        
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

class LogadoForm(UserCreationForm):
    drt = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your DRT',
        'class': 'container'
    }))
    

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email address',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

class UsuarioModelForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['drt', 'nome', 'cargo', 'perfil_acesso']

class LoginModelForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['drt', 'nome', 'cargo', 'perfil_acesso']
        ordering = ['nome']

INPUT_CLASSES = ''

# class EditUsuarioForm(forms.ModelForm):
#     class Meta:
#         model = UsuarioModelForm
#         private_fields = ('drt',)
#         fields = ('drt', 'nome', 'cargo', 'perfil_acesso')
#         widgets = {
#             'drt': forms.TextInput(attrs={
#                 'class': INPUT_CLASSES
#             }),
#             'nome': forms.TextInput(attrs={
#                 'class': INPUT_CLASSES
#             }),
#             'cargo': forms.TextInput(attrs={
#                 'class': INPUT_CLASSES
#             }),
#             'perfil_acesso': forms.TextInput(attrs={
#                 'class': INPUT_CLASSES
#             })
#         }
