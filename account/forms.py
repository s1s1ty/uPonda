from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError

from .models import Profile


# join form
class UserJoinForm(forms.ModelForm):
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email'
    }))
    username = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username'
    }))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Create a password'
    }))

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise ValidationError('Password too short')
        return password


# login form
class UserLoginForm(forms.Form):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username'
    }))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password'
    }))


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('user_type',)
