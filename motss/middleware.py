from django.http import HttpResponseRedirect, HttpResponse, HttpResponseServerError
from django.template import Context, loader
from member.exceptions import UserException, DuplicateException, \
	RegisterException, NoUserLoginException, WrongPasswordException,\
	NoSuchUserException, FollowedException, FollowDeniedException
from post.exceptions import PostException, IllegalContentException, \
	NoSuchThreadException, ThreadDeletedException, ThreadClosedException, \
	AttachOverSizedException, AttachUnsupportException
import json


class MotssMiddleware(object):
	def process_exception(self, request, exception):
		print exception
		print "======"
		if isinstance(exception, UserException):
			msg = exception.msg
		elif isinstance(exception, PostException):
			msg = exception.msg
		else:
			msg = exception.args

		if request.is_ajax():
			return HttpResponseServerError(json.dumps({'msg':msg}), mimetype="application/json")

		t = loader.get_template('error.html')
		context = Context({'msg':msg})
		return HttpResponseServerError(t.render(context))