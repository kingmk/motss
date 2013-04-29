USER_ERRCODE = {
	0 : 'Exception occurs in member app.', # UserException
	1 : 'Unable to register, the username exists.', # DuplicateException
	2 : 'Incorrectly fill in registration information.', # RegisterException
	3 : 'Unable to login with a wrong username. ', # NoUserLoginException
	4 : 'Unable to login with wrong password.', # WrongPasswordException
	5 : 'The user does not exist.', # NoSuchUserException
	6 : 'The user has already been followed.', # FollowedException
	7 : 'The user forbid others to follow him.', # FollowDeniedException
	8 : 'Cannot follow yourself.' # FollowSelfException
}

class UserException(Exception):
	code = 0
	cause = None
	msg = ''
	def __init__(self, msg=None, cause=None):
		self.cause = cause
		if msg is None:
			self.msg = USER_ERRCODE[self.code]
		else:
			self.msg = msg
		super(UserException, self).__init__('%s, caused by:%s'%(self.msg, str(self.cause)))

class DuplicateException(UserException):
	code = 1
	def __init__(self, cause=None, username=''):
		msg = '%s With username: %s'%(USER_ERRCODE[self.code], username)
		super(DuplicateException, self).__init__(msg, cause)

class RegisterException(UserException):
	code = 2
	def __init__(self, cause=None, note=''):
		msg = '%s Note: %s'%(USER_ERRCODE[self.code], note)
		super(RegisterException, self).__init__(msg, cause)

class NoUserLoginException(UserException):
	code = 3
	def __init__(self, cause=None, username=''):
		msg = '%s With username: %s'%(USER_ERRCODE[self.code], username)
		super(NoUserLoginException, self).__init__(msg, cause)

class WrongPasswordException(UserException):
	code = 4
	def __init__(self, cause=None):
		msg = USER_ERRCODE[self.code]
		super(WrongPasswordException, self).__init__(msg, cause)

class NoSuchUserException(UserException):
	code = 5
	def __init__(self, cause=None, username=''):
		msg = '%s User "%s" not exists'%(USER_ERRCODE[self.code], username)
		super(NoSuchUserException, self).__init__(msg, cause)

class FollowedException(UserException):
	code = 6
	def __init__(self, cause=None, username=''):
		msg = '%s Follow user: %s'%(USER_ERRCODE[self.code], username)
		super(FollowedException, self).__init__(msg, cause)

class FollowDeniedException(UserException):
	code = 7
	def __init__(self, cause=None, username=''):
		msg = '%s Denied by user: %s'%(USER_ERRCODE[self.code], username)
		super(FollowDeniedException, self).__init__(msg, cause)

class FollowSelfException(UserException):
	code = 8
	def __init__(self, cause=None):
		msg = USER_ERRCODE[self.code]
		super(FollowSelfException, self).__init__(msg, cause)
