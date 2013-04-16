from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse

from short_message.models import Message
from short_message.models import Chat

def index(request):
    chat_list = Chat.objects.all().order_by('last_time')[:10]
    context = {'chat_list':chat_list}
    return render(request, 'message/index.html', context)

def chat(request,cid):    
    latest_message_list = Message.objects.filter(cid=cid).order_by('send_time')
    count = latest_message_list.count()
    latest_message_list = latest_message_list[count-5:]
    chat_list = Chat.objects.filter(cid=cid)
    for e in chat_list:
        chat = e
    context = {'latest_message_list': latest_message_list,'chat':chat}
    return render(request, 'message/chat.html', context)
