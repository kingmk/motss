from django.db import transaction
from member.models import MotssUser, MotssProfile, MotssFollow
from django.db import IntegrityError
from member.exceptions import UserException, DuplicateException, \
	RegisterException, NoUserLoginException, WrongPasswordException,\
	FollowNoUserException, FollowedException, FollowDeniedException,\
	FollowSelfException


class MemberManager:
	def raise_integrity_error(self, error, username):
		code = error.args[0]
		if code == 1062:
			raise FollowedException(cause=error, username=username)
		elif code == 1452:
			raise FollowNoUserException(cause=error, username=username)
		else :
			raise UserException(cause=error)


	def follow(self, user, follow_id):
		if user.id==follow_id:
			raise FollowSelfException()

		mfollow = MotssFollow(user=user, follow_id=follow_id)
		try:
			mfollow.save()
		except IntegrityError, ie:
			self.raise_integrity_error(ie, str(follow_id))
		except Exception, e:
			raise UserException(cause=e)

		return mfollow

	def unfollow(self, user, follow_id):
		if user.id==follow_id:
			raise FollowSelfException()
		qt = MotssFollow.objects.filter(user=user, follow_id=follow_id)
		if qt.exists():
			qt.delete()
		else:
			raise UserException()


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
