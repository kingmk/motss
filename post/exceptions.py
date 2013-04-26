POST_ERRCODE = {
	0 : 'Exception occurs in post app.', # PostException
	1 : 'The post contains illegal content.', # IllegalContentException
	2 : 'No such thread exists.', # NoSuchThreadException
	3 : 'The thread has been deleted.', # ThreadDeletedException
	4 : 'The thread has been closed, and cannot be replied.', # ThreadClosedException
	5 : 'The uploaded attach is too large.', # AttachOverSizedException
	6 : 'The uploaded attach type is not supported.' # AttachUnsupportException
}

class PostException(Exception):
	code = 0
	cause = None
	msg = None
	def __init__(self, msg=None, cause=None):
		self.cause = cause
		if msg is None:
			self.msg = POST_ERRCODE[self.code]
		else:
			self.msg = msg
		super(PostException, self).__init__('%s, caused by:%s'%(self.msg, str(self.cause)))

class IllegalContentException(PostException):
	code = 1
	malcontent = ''
	def __init__(self, cause=None, malcontent=''):
		self.malcontent = malcontent
		msg = '%s With illegal content:%s'%(POST_ERRCODE[self.code], str(self.malcontent))
		super(IllegalContentException, self).__init__(msg, cause)

class NoSuchThreadException(PostException):
	code = 2
	tid = 0
	def __init__(self, cause=None, tid=0):
		self.tid = tid
		msg = '%s ThreadId:%s'%(POST_ERRCODE[self.code], str(self.tid))
		super(NoSuchThreadException, self).__init__(msg, cause)

class ThreadDeletedException(PostException):
	code = 3
	tid = 0
	def __init__(self, cause=None, tid=0):
		self.tid = tid
		msg = '%s ThreadId:%s'%(POST_ERRCODE[self.code], str(self.tid))
		super(ThreadDeletedException, self).__init__(msg, cause)

class ThreadClosedException(PostException):
	code = 4
	tid = 0
	def __init__(self, cause=None, tid=0):
		self.tid = tid
		msg = '%s ThreadId:%s'%(POST_ERRCODE[self.code], str(self.tid))
		super(ThreadClosedException, self).__init__(msg, cause)

class AttachOverSizedException(PostException):
	code = 5
	size = 0
	def __init__(self, cause=None, size=0):
		self.size = size
		msg = '%s Size:%s'%(POST_ERRCODE[self.code], str(self.size))
		super(AttachOverSizedException, self).__init__(msg, cause)

class AttachUnsupportException(PostException):
	code = 6
	attach_type = 'unknown'
	def __init__(self, cause=None, attach_type='unknown'):
		self.attach_type = attach_type
		msg = '%s Size:%s'%(POST_ERRCODE[self.code], str(self.attach_type))
		super(AttachUnsupportException, self).__init__(msg, cause)
