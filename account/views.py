from django.contrib import messages
from django.contrib.auth import (
    authenticate,
    login,
)
from django.shortcuts import render, redirect
from django.views import generic

from .forms import UserJoinForm, UserLoginForm, ProfileForm


class UserJoinView(generic.View):
    form_classes = {
        'user_form': UserJoinForm,
        'profile_form': ProfileForm
    }
    template_name = 'form.html'

    def get(self, request):
        form = self.form_classes
        context = {
            'form': form,
            'type': 'join'
        }
        return render(request, self.template_name, context)

    def post(self, request):
        err = False
        form = self.form_classes
        user_form = form.get('user_form')(request.POST)
        profile_form = form.get('profile_form')(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)

            username = user_form.cleaned_data['username']
            password = user_form.cleaned_data['password']
            user.set_password(password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user_id = user
            profile.save()

            user_login = authenticate(username=username, password=password)
            if user_login is not None:
                if user_login.is_active:
                    request.session.set_expiry(86400)
                    login(request, user_login)
                    messages.success(request, 'Registration Complete')
                    if user_login.is_staff:
                        return redirect('/admin/')
                    return redirect('/')
        else:
            messages.error(request, 'Password is too short or Email is incorrect')
            user_form = self.form_classes

        context = {
            'title': 'Registration',
            'form': user_form,
            'profile_form': profile_form,
            'type': 'join'
        }
        return render(request, 'form.html', context)


class UserLoginView(generic.View):
    template_name = 'form.html'
    form_class = UserLoginForm

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form, 'type': 'login'})

    def post(self, request):
        form = self.form_class(request.POST)

        username = request.POST.get('username')
        password = request.POST.get('password')

        if form.is_valid:
            user = authenticate(username=username, password=password)
            if user is not None and user.is_active:
                request.session.set_expiry(86400)
                login(request, user)
                messages.success(request, "Login SuccessFull")
                if user.is_staff:
                    return redirect('/admin/')
                return redirect('/')
            else:
                messages.error(request, "Incorrect Username or Password")

            context = {
                'title': 'Login',
                'form': form,
                'type': 'login'
            }
            return render(request, self.template_name, context)
