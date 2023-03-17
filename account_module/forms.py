from django import forms
from django.core import validators
from django.core.exceptions import ValidationError


class RegisterForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'type': 'email',
        }),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator,
        ],
    )
    username = forms.CharField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'type': 'text',
        }),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator,
        ],
        error_messages={
            'unique': 'this username taken'
        }
    )
    fullname = forms.CharField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'type': 'text',
        }),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator,
        ],
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'type': 'password',
            'id': "password-field",
        }),
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'type': 'password',
            'id': "password-field",
        }),
    )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password == confirm_password:
            return confirm_password

        raise ValidationError('password and confirm password not same!')


class LoginForm(forms.Form):
    email = forms.CharField(
        label='Email or Username',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'type': "text",
        }),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'type': "password",
            'id': "password-field",
        }),
    )
