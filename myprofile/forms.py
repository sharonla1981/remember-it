from django.forms import ModelForm
from .models import *

"""class ProfileForm(ModelForm):
    def __init__(self):
        session_key = self.request.COOKIES.get('sessionid')
    class Meta:
        model = UserExternalTool
        fields = ['externalTool']
   """