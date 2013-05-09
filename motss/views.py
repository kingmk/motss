from django.http import HttpResponseRedirect, HttpResponse, HttpResponseServerError
from django.template import Context, loader
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate
from asyncq.task import add
from member.models import MotssUser
from member.membermanager import MemberManager
import sys

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def home(request):
	if request.user.is_authenticated():
		print request.user

	return render(request,'home.html')

def test(request):

	return render(request,'test.html')

#def error_view(request):
#	t = loader.get_template('error.html')
#	return HttpResponseServerError(t.render(Context({})))