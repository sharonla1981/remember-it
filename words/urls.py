from django.urls import path
from . import views

app_name = 'words'
urlpatterns = [
    # /words/
    path('',views.show_words,name='index'),
    #path('',views.IndexView.as_view(),name='index'),

    # words/<word_id>/
    path('word/<int:pk>',views.DetailView.as_view(),name='detail'),

    # words/add/<word_text>/
    path('add/<word_text>/',views.add),

    # words/show_words/
    path('show_words/',views.show_words,name='index'),
]
