from django.http import HttpResponseRedirect, HttpResponse, HttpResponseServerError
from django.template import Context, loader
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login
from member.models import MotssUser
from member.membermanager import MemberManager
import json


def get_client_ip(request):
	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	if x_forwarded_for:
		ip = x_forwarded_for.split(',')[0]
	else:
		ip = request.META.get('REMOTE_ADDR')
	return ip

def viewlogin(request):
	return render(request,'login.html')

def dologin(request):
	username = request.REQUEST['username']
	password = request.REQUEST['password']

	member_manager = MemberManager()
	user = member_manager.authenticate(username=username, password=password)
	user.loginip = get_client_ip(request)
	login(request, user)
	response_data = {}
	response_data['code'] = 0
	return HttpResponse(json.dumps(response_data), mimetype="application/json")