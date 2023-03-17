from django.contrib import admin
from . import models


# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['email']


admin.site.register(models.User, UserAdmin)
