from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.db import models


# Create your models here.

class User(AbstractUser):
    username_validator = ASCIIUsernameValidator()
    username = models.CharField(max_length=150, unique=True, validators=[username_validator],)
    full_name = models.CharField(max_length=300, verbose_name='fullName', null=True, blank=True)

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def save(self, *args, **kwargs):
        self.username = self.username.lower()
        return super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.username
