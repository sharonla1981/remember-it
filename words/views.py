from django.views import generic
from django.http import JsonResponse
from .models import Word
from django.contrib.auth.models import User
from myprofile.models import UserExternalTool,UserDefaultWordSet,UserLanguages
from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse

from .external.ql2 import QuizletDirect
from .external.oxford_api import oxford_api
from .external.google_translate_api import GoogleTranslate

import json


@method_decorator(login_required, name='dispatch')
class IndexView(generic.ListView):
    template_name = 'words/index.html'
    context_object_name = 'all_words'

    def get_queryset(self):
        return Word.objects.all()

@method_decorator(login_required, name='dispatch')
class DetailView(generic.DetailView):
    model = Word
    template_name = 'words/detail.html'

@login_required
def add(request,word_text):
    default_word_set_id = ''
    current_user_pk = request.user.pk
    current_user = User.objects.get(pk=current_user_pk)
    user_languages = UserLanguages.objects.get(user=current_user)
    learning_language = user_languages.learning_language.alpha_2
    preferred_language = user_languages.preferred_language.alpha_2
    external_tool = UserExternalTool.objects.get(user_id=current_user_pk)
    #create Quizlet instance
    user_access_info = external_tool.user_access_info
    ql = QuizletDirect(user_access_info)
    try:
        default_word_set_id = UserDefaultWordSet.objects.get(user_id=current_user_pk).default_set_id
        #check if the set exists in quizlet (to make sure that it wasn't deleted by the user)
        if default_word_set_id != '':
            user_set_error = ql.get_set(default_word_set_id)['error']
            if user_set_error != None:
                default_word_set_id = ''
                raise Exception('Set Does not exist')
    except:
        pass



    #get oxfrod dictionary translation
    translation = ''
    data = {}
    try:
        #in case oxford return an example it would replace the data pushed to quizlet
        oxford = oxford_api(learning_language,preferred_language)
        result = oxford.get_original_and_translation_example(word_text)
        translation = result['translation']
        if result['original_language_exmaple'] != '':
            word_text = result['original_language_exmaple']
            translation = result['destination_language_exmaple']

    except:
        #google tranlate is the fallback translation service
        google = GoogleTranslate(preferred_language)
        translation = google.translate_text(word_text)['translation']

    # if the user doesn't have a quizlet set_id saved in our system, a new set will be created and be used
    if (default_word_set_id == None or default_word_set_id == '') and translation != '':
        new_set = ql.add_set('iRemember-It', ['sample-term',word_text],['sample-translation',translation],learning_language,preferred_language)
        default_word_set_id = new_set['set_id']
        print(new_set)
        UserDefaultWordSet.objects.update_or_create(user=current_user,defaults={'default_set_id':default_word_set_id})

        data = {'ws_id': default_word_set_id, 'word': word_text, 'translation': translation}

        return JsonResponse(data)

    if translation != '' and default_word_set_id != None:
        #quizlet push word to set
        set = ql.add_term_to_set(default_word_set_id,word_text,translation)
        data = {'ws_id':default_word_set_id,'word':word_text,'translation':translation}

        print(data)


    return JsonResponse(data)

@login_required
def show_words(request):
    current_user_pk = request.user.pk
    #get user default word set
    try:
        default_word_set_id = UserDefaultWordSet.objects.get(user_id=current_user_pk).default_set_id
    except:
        default_word_set_id = 0
    #get user external tool, if it doesn't exist, redirect to external_tools page
    try:
        external_tool = UserExternalTool.objects.get(user_id=current_user_pk)
    except:
        #redirect to on-boarding in case the user is new and doesn't have an external tool (quizlet) connected in the account.
        return redirect(reverse('myprofile:onboarding'))
    user_access_info = external_tool.user_access_info
    ql = QuizletDirect(user_access_info)
    sets = ql.get_sets()
    return render(request,'words/sets_from_quizlet.html',{'sets': sets,'default_word_set_id':default_word_set_id})
