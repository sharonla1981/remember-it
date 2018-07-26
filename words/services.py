from django import forms
from .models import Word,Country,Language
from externaltools.models import ExternalTool
from myprofile.models import UserExternalTool

from service_objects.services import Service

from .external.ql import Quizlet

class WordList(Service):
    #sets = []
    def get_all_sets(self,user):

