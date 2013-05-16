from member.exceptions import LoginRequiredException
import json


def check_authenticate(request):
	if not request.user.is_authenticated():
		raise LoginRequiredException()