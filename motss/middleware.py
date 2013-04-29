from django.http import HttpResponseRedirect, HttpResponse, HttpResponseServerError
from django.template import Context, loader
from member.exceptions import UserException, DuplicateException, \
	RegisterException, NoUserLoginException, WrongPasswordException,\
	NoSuchUserException, FollowedException, FollowDeniedException
from post.exceptions import PostException, IllegalContentException, \
	NoSuchThreadException, ThreadDeletedException, ThreadClosedException, \
	AttachOverSizedException, AttachUnsupportException


class MotssMiddleware(object):
	def process_exception(self, request, exception):
		if isinstance(exception, UserException):
			msg = exception.msg
		elif isinstance(exception, PostException):
			msg = exception.msg
		else:
			msg = exception.args
		t = loader.get_template('error.html')
		context = Context({'msg':msg, 'is_ajax':request.is_ajax()})
		return HttpResponseServerError(t.render(context))