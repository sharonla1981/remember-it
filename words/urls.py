from django.urls import path
from . import views

app_name = 'words'
urlpatterns = [
    # /words/
    # if nothing specified it goes to show_words - it redirects to connect a new ExternalTool in case there's non for the user
    path('',views.show_words,name='index'),

    # words/<word_id>/
    path('word/<int:pk>',views.DetailView.as_view(),name='detail'),

    # words/add/<word_text>/
    path('add/<word_text>/',views.add),

    # words/show_words/
    path('show_words/',views.show_words,name='index'),
]
