from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse

def index(request):
    chat_list=1
    context = {'chat_list':chat_list}
    return render(request, 'index/index.html', context)
