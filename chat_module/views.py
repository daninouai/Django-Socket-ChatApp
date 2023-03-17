from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView
from .models import Room, Message
from django.utils.decorators import method_decorator


# Create your views here.

class HomeView(View):
    def get(self, request: HttpRequest):
        rooms = Room.objects.all()
        context = {
            'rooms': rooms
        }
        return render(request, 'chat_module/index_page.html', context)


@method_decorator(login_required, name='dispatch')
class EnterRoomView(DetailView):
    model = Room
    template_name = 'chat_module/chat_room_page.html'

    def get_context_data(self, **kwargs):
        context = super(EnterRoomView, self).get_context_data(**kwargs)
        context['message'] = Message.objects.filter(room=self.object.id)
        return context


def add_message(request: HttpRequest):
    if request.user.is_authenticated:
        room = request.GET.get('mass')
        context = {
            'message': Message.objects.filter(room=room)
        }

        return render(request, 'chat_module/components/chat_message_component.html', context)

    return HttpResponse('response')
