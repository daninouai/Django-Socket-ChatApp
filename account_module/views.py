from django.contrib.auth.base_user import BaseUserManager
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.views import View
from .models import User
from django.http import HttpRequest
from django.contrib.auth import login, logout
import string
from .forms import RegisterForm, LoginForm

# Create your views here.

user = get_user_model()


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        context = {
            'register_form': register_form
        }

        return render(request, 'account_module/register_page.html', context)

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            username = register_form.cleaned_data.get('username').lower()
            user_email = register_form.cleaned_data.get('email')
            user_fullname = register_form.cleaned_data.get('fullname')
            user_password = register_form.cleaned_data.get('password')
            username_taken: bool = User.objects.filter(username=username).exists()
            user_by_email: bool = User.objects.filter(email=user_email).exists()
            user_by_username: bool = User.objects.filter(username=user_email).exists()
            if user_by_email:
                register_form.add_error('email', 'This email has a user account')
            if user_by_username:
                register_form.add_error('email', 'This user name already exists')
            if username_taken:
                register_form.add_error('username', 'This user name already exists')
            else:
                new_user = User(
                    email=user_email,
                    username=username,
                    full_name=user_fullname,
                    is_active=True,
                )
                new_user.set_password(user_password)
                new_user.save()
                return redirect(reverse('login_page'))

        context = {
            'register_form': register_form
        }

        return render(request, 'account_module/register_page.html', context)


class LoginView(View):
    def get(self, request):
        login_form = LoginForm()
        context = {
            'login_form': login_form
        }

        return render(request, 'account_module/login_page.html', context)

    def post(self, request: HttpRequest):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_email_username = login_form.cleaned_data.get('email')
            user_pass = login_form.cleaned_data.get('password')
            user: User = User.objects.filter(email__iexact=user_email_username).first()
            if user is None:
                user: User = User.objects.filter(username=user_email_username).first()
            if user is not None:
                is_password_correct = user.check_password(user_pass)
                if is_password_correct:
                    login(request, user)
                    return redirect(reverse('home_page'))
                else:
                    login_form.add_error('email', 'The username or password is incorrect')
            else:
                login_form.add_error('email', 'The username or password is incorrect')

        context = {
            'login_form': login_form
        }

        return render(request, 'account_module/login_page.html', context)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('login_page'))
