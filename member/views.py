from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse


def index(request):
    latest_member_list = []
    context = {'latest_member_list': latest_member_list}
    return render(request, 'member/index.html', context)
