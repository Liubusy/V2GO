#coding=utf-8

from django.contrib.auth.backends import ModelBackend
from forum.models import ForumUser

class EmailAuthBackend(ModelBackend):

	def authenticate(self, email=None, password=None):
		try:
			user = ForumUser.objects.get(email=email)
			if user.check_password(password):
				return user
		except ForumUser.DoesNotExist:
			return None

	def get_user(self, user_id):
		try:
			return ForumUser.objects.get(pk=user_id)
		except ForumUser.DoesNotExist:
			return None