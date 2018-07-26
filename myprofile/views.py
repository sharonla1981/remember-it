from django.views import generic
from django.http import JsonResponse
from .models import UserExternalTool,UserDefaultWordSet
from externaltools.models import ExternalTool
from django.shortcuts import render,redirect
from django.views.generic.base import RedirectView,View
from django.views.generic.edit import CreateView,UpdateView
from . import forms
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.models import User
from .models import UserProfile

from importlib import import_module
from django.conf import settings

from words.external.ql import Quizlet

import base64

#quizlet class instance
encoded_auto = b64_auth_code = str(base64.b64encode(bytes('PuEmP48Pxg:xqtWHJkwKzR24um6rWFBeK', "utf-8")),encoding="utf-8")
ql = Quizlet('PuEmP48Pxg',encoded_auto,'http://www.iremember-it.com/myprofile/external_tool_redirect/')

@method_decorator(login_required, name='dispatch')
class MyProfile(CreateView):
    model = UserProfile
    fields = ['language']

@method_decorator(login_required, name='dispatch')
class AddUserExternalTool(CreateView):
    model = UserExternalTool
    fields = ['external_tool']

    #get the user_token from the session and populate the user_token field on submit
    def form_valid(self, form):
        #user_token = self.request.session['code']
        user_access_info = self.request.session['access_info']
        form.instance.user_access_info = user_access_info
        response = super(AddUserExternalTool, self).form_valid(form)
        if self.request.is_ajax():
            print(form.cleaned_data)
            data = {
                'message': "Successfully submitted form data."
            }
            return JsonResponse(data)
        else:
            return response


class ApproveExternalTool(RedirectView):

    def get(self,request,tool_id):

        user_access_info = ''
        self.url = reverse('myprofile:detail')

        #if there's no access_info in the session it will redirect to the external tool (quizlet)
        try:
            user_access_info = request.session['access_info']
        except:
            self.url = ql.generate_auth_url('read write_set')[0]

        if user_access_info != '':
            user_external_tool = UserExternalTool()
            current_user_pk = self.request.user.pk

            external_tool = ExternalTool.objects.get(pk=tool_id)
            user = User.objects.get(pk=current_user_pk)
            user_external_tool.user = user
            user_external_tool.external_tool = external_tool
            user_external_tool.user_access_info = user_access_info
            # UserExternalTool.objects.create(external_tool=external_tool,user=user,user_access_info=user_access_info)
            user_external_tool.save()
            self.url = reverse('myprofile:detail')
        return redirect(self.url)


class ExternalToolApproved(View):
    def get(self,request):
        code = request.GET.get('code')
        ql.request_token(code)
        #get the user_token from the external tool (quizlet) and store it in the session
        print(ql.access_info)
        request.session['access_info'] = ql.access_info
        request.session.save()
        #return redirect(reverse('myprofile:approve-user-external_tool_with_id',1))
        return redirect('http://www.iremember-it.com/myprofile/approve_external_tool/1/')


@method_decorator(login_required, name='dispatch')
class DetailView(generic.DetailView):
    model = UserExternalTool
    context_object_name = 'my_external_tools'
    template_name = 'myprofile/detail.html'

@method_decorator(login_required, name='dispatch')
class ExternalTools(generic.ListView):
    template_name = 'myprofile/externaltools.html'
    context_object_name = 'all_tools'

    def get_queryset(self):
        current_user_pk = self.request.user.pk

        query = "select row_number() over () rownum," \
                "et.id,et.name, \
		case when met.user_access_info is not null and au.id = {} then 'Connected' else 'Not connected' end connected \
        from externaltools_externaltool et \
        left join myprofile_userexternaltool met on et.id = met.external_tool_id and met.user_id = {} left join auth_user au on met.user_id = au.id".format(current_user_pk,current_user_pk)
        print(query)
        return ExternalTool.objects.raw(query)

#@method_decorator(login_required, name='dispatch')
def setUserDefaultWordSet(request,set_id):
    current_user_pk = request.user.pk
    user = User.objects.get(pk=current_user_pk)
    user_default_word_set,created = UserDefaultWordSet.objects.update_or_create(user=user,defaults={'default_set_id':set_id})
    #user_default_word_set.default_set_id = set_id
    user_default_word_set.save()
    data = {'update': 1}
    return JsonResponse(data)