from account_module.models import User
from django.db import models


# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=225, verbose_name='room name')
    slug = models.SlugField(unique=True, verbose_name='slug')

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'room'
        verbose_name_plural = 'rooms'


class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name='room')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='user')
    content = models.TextField(verbose_name='message content')
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'message'
        verbose_name_plural = 'messages'
        ordering = ('date_added',)
