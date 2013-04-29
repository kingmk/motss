from django.db import transaction
from member.models import MotssUser, MotssProfile, MotssFollow
from django.db import IntegrityError
from django.db.models import F
from member.exceptions import UserException, DuplicateException, \
	RegisterException, NoUserLoginException, WrongPasswordException,\
	NoSuchUserException, FollowedException, FollowDeniedException,\
	FollowSelfException


class MemberManager:
	def raise_integrity_error(self, error, username):
		code = error.args[0]
		if code == 1062:
			raise FollowedException(cause=error, username=username)
		elif code == 1452:
			raise NoSuchUserException(cause=error, username=username)
		else :
			raise UserException(cause=error)

	@transaction.commit_on_success
	def follow(self, user, follow_id):
		if user.id==follow_id:
			raise FollowSelfException()

		try:
			followee = MotssUser.objects.filter(id=follow_id).get()
		except Exception, e:
			raise NoSuchUserException(cause=e, username=str(follow_id))

		mfollow = MotssFollow(user=user, follow_id=follow_id)
		try:
			mfollow.save()
		except IntegrityError, ie:
			self.raise_integrity_error(ie, str(follow_id))
		except Exception, e:
			raise UserException(cause=e)

		try:
			user.inc_follow(1)
			followee.inc_follower(1)
		except Exception, e:
			raise UserException(cause=e)
		return mfollow

	@transaction.commit_on_success
	def unfollow(self, user, follow_id):
		if user.id==follow_id:
			raise FollowSelfException()

		try:
			followee = MotssUser.objects.filter(id=follow_id).get()
		except Exception, e:
			raise NoSuchUserException(cause=e, username=str(follow_id))

		qt = MotssFollow.objects.filter(user=user, follow_id=follow_id)
		if qt.exists():
			qt.delete()
		else:
			raise UserException()

		try:
			user.inc_follow(-1)
			followee.inc_follower(-1)
		except Exception, e:
			raise UserException(cause=e)

	def has_follow(self, user, follow_id):
		qt = MotssFollow.objects.filter(user=user, follow_id=follow_id)
		return qt.exists()

	def get_user_follows(self, user, start, count):
		follow_relations = MotssFollow.objects.filter(user_id=user.id).order_by('-createtime')[start:start+count].select_related()
		follows = []
		for relation in follow_relations:
			follows.append(relation.follow)
		return follows

	def get_user_followers(self, followee, start, count):
		follow_relations = MotssFollow.objects.filter(follow_id=followee.id).order_by('-createtime')[start:start+count].select_related()
		follows = []
		for relation in follow_relations:
			follows.append(relation.user)
		return follows
