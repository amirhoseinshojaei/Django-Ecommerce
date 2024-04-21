from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegistrationForm(UserCreationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password Confirm'}))

    class Meta:
        model = CustomUser
        fields = ['email','username','password1','password2']