from django.http import HttpResponseRedirect, HttpResponse, HttpResponseServerError
from django.template import Context, loader
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login

from motss.common import check_authenticate
from post.models import Thread, Post, Test, Attachment, TagThread
from post.postmanager import PostManager
from post.xssparser import XssParser
import json


def create_thread(request):
	check_authenticate(request)
	subject = request.POST['title']
	tags = request.POST['tags'].split()
	content = request.POST['content']
	author = request.user

	pm = PostManager()
	pm.create_thread(author, subject, content, 1, [], tags)

	response_data = {}
	response_data['code'] = 0
	return HttpResponse(json.dumps(response_data), mimetype="application/json")