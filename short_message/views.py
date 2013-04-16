from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse

from short_message.models import Message
from short_message.models import Chat

def index(request):
    latest_message_list = Message.objects.filter(cid=1).order_by('-send_time')[:5]
    latest_chat_list = Chat.objects.order_by('-last_time')[:5]
    context = {'latest_message_list': latest_message_list,'latest_chat_list':latest_chat_list}
    return render(request, 'message/index.html', context)
