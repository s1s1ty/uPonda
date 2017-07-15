from django.contrib.auth import (
	authenticate,
	login,
	logout,
	get_user_model,
	)
from django.shortcuts import render, HttpResponse, redirect
from django.views import generic

from .forms import UserJoinForm, UserLoginForm

class UserJoinView(generic.View):
	form_class = UserJoinForm
	template_name = 'form.html'

	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form': form, 'type': 'join'})

	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid():
			user = form.save(commit=False)

			# normalized data
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()

			# auto login after successfully registration
			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					login(request, user)
					return redirect('/')

		return render(request, self.template_name, {'form': form, 'type': 'join'})

class UserLoginView(generic.View):
	template_name = 'form.html'
	form_class = UserLoginForm
	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form': form, 'type': 'login'})

	def post(self, request):
		form = self.form_class(request.POST)
		if form.is_valid():
			user = form.authenticate()
			if user is not None:
				login(request, user)
				return redirect('/')
		return render(request, self.template_name, {'form': form, 'type': 'login'})


def index(request):
	return render(request, 'index.html', {})


