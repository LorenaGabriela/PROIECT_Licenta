from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms.widgets import TextInput, PasswordInput
from .models import Pacienti, Mamografii


class MedicRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2' ]


class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


class PacientiForm(forms.ModelForm):
    class Meta:
        model = Pacienti
        fields = ['nume_pacient', 'prenume_pacient', 'email_pacient', 'telefon_pacient', 'data_nastere', 'sex_pacient']


class MamografiiForm(forms.ModelForm):
    class Meta:
        model = Mamografii
        fields = ['nume_pacient', 'file', 'description', 'data_incarcare']