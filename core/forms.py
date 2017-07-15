from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import authenticate

# join form
class UserJoinForm(forms.ModelForm):
	email    = forms.EmailField(label='', widget=forms.TextInput(attrs={
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
		model  = User
		fields = ['username', 'email', 'password']

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

	def authenticate(self):
		username = self.cleaned_data["username"]
		password = self.cleaned_data["password"]
		if username and password:
			return authenticate(username=username, password=password)

	def clean(self, *args, **kwargs):
		user = self.authenticate()
		if not user:
			raise forms.ValidationError("User doesn't Exist or Incorrect Password.")
		if not user.is_active:
			raise forms.ValidationError("This user is no longer active.")
		return super(UserLoginForm, self).clean(*args, **kwargs)
