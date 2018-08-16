# coding=utf-8

from django.contrib.auth.backends import ModelBackend

from .models import User


class ModelBackend(ModelBackend):

    def authenticate(self, username=None, password=None, **kwargs):
        if not username is None:
            try:
                user = User.objects.get(email=username)
                if user.check_password(password):
                    return user
            except User.DoesNotExist:
                pass
