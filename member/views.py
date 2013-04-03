from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse

from member.models import Member

def index(request):
    latest_member_list = Member.objects.order_by('-regdate')[:5]
    context = {'latest_member_list': latest_member_list}
    return render(request, 'member/index.html', context)
