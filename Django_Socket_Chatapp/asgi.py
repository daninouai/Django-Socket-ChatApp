"""
ASGI config for Django_Socket_Chatapp project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

# set the type of connection with ProtocolTypeRouter => ws or wss

import chat_module.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Django_Socket_Chatapp.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            chat_module.routing.websocket_urlpatterns
        )
    )
})
