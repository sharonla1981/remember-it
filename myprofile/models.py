from django.db import models
from django.core.exceptions import ValidationError
from django import forms
from django.contrib.postgres.fields import ArrayField
from externaltools.models import ExternalTool
from words.models import Language
from importlib import import_module
from django.conf import settings
from django.contrib.sessions.models import Session
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.auth.models import User

from django_userforeignkey.models.fields import UserForeignKey


class UserExternalTool(models.Model):
    external_tool = models.ForeignKey(ExternalTool,on_delete=models.DO_NOTHING)
    user = UserForeignKey(auto_user_add=True)
    user_access_info = models.CharField(max_length=5000,null=True)

    def __str__(self):
        return self.external_tool.name

class UserDefaultWordSet(models.Model):
    user = UserForeignKey(auto_user_add=True)
    default_set_id = models.IntegerField(null=True)

class UserProfile(User):
    language = models.ForeignKey(Language,null=True,on_delete=models.DO_NOTHING)

class UserLanguages(models.Model):
    user = UserForeignKey(auto_user_add=True)
    learning_language = models.ForeignKey(Language, null=True, on_delete=models.DO_NOTHING,related_name='learning')
    preferred_language = models.ForeignKey(Language, null=True, on_delete=models.DO_NOTHING,related_name='preffered')

    def clean(self, *args, **kwargs):

        if self.learning_language == self.preferred_language:
            raise ValidationError("Please select different languages")
        super(UserLanguages,self.clean(*args, **kwargs))