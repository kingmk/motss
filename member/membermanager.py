from django.db import transaction
from member.models import MotssUser, MotssProfile, MotssFollow

class MemberManager:
	def follow(self, user, follow_id):
		if user.id==follow_id:
			return None

		mfollow = MotssFollow(user=user, follow_id=follow_id)
		try:
			mfollow.save()
		except Exception, e:
			return None

		return mfollow

	def unfollow(self, user, follow_id):
		if user.id==follow_id:
			return False
		qt = MotssFollow.objects.filter(user=user, follow_id=follow_id)
		if qt.exists():
			qt.delete()
			return True

		return False


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
