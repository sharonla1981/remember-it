from django import forms
from .models import UserLanguages

"""class ProfileForm(ModelForm):
    def __init__(self):
        session_key = self.request.COOKIES.get('sessionid')
    class Meta:
        model = UserExternalTool
        fields = ['externalTool']
   """

class UserLanguagesForm(forms.ModelForm):
    class Meta:
        model = UserLanguages
        fields = ['learning_language','preferred_language']
        labels = {
            'learning_language': 'I am Learning',
            'preferred_language': 'My Favorite Language'
        }
        widgets = {
            'learning_language': forms.Select(attrs={
                'id': 'learning_language',
                'class': 'form-control',
                'required': True,
            }),
            'preferred_language': forms.Select(attrs={
                'id': 'preferred_language',
                'class': 'form-control',
                'required': True,
            }),
        }
