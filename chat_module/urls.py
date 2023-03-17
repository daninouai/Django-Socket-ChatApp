from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home_page'),
    path('chat/<slug:slug>/', views.EnterRoomView.as_view(), name='enter_room'),
    path('chat/add-message', views.add_message, name='add_message'),
]
