from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse

from member.models import Member

def index(request):

    return render(request, 'index/index.html')

def check(request):
    try_name=request.POST['username']
    try_password=request.POST['password']
    login_user_list = Member.objects.filter(username=try_name).order_by('-regdate')[:1]
    if not login_user_list:
        return render(request,'index/error.html')
    elif (try_password==login_user_list[0].password):        
        return render(request,'index/success.html')
    else:
        return render(request,'index/error.html')
    # return render(request,'member/index.html',context)
