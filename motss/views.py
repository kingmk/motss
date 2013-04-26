from django.http import HttpResponseRedirect, HttpResponse, HttpResponseServerError
from django.template import Context, loader
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
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

def test(request):
	print "test"
	s = 'ddd'+1
	mm = MemberManager()
	user = MotssUser.objects.all()[1]
	mm.follow(user, 11111)
	return render(request,'test.html')

#def error_view(request):
#	t = loader.get_template('error.html')
#	return HttpResponseServerError(t.render(Context({})))