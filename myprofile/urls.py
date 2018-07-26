from django.urls import path
from . import views
#from myprofile.views import AddUserExternalTool


app_name = 'myprofile'
urlpatterns = [
    # /myprofile/
    path('',views.MyProfile.as_view(),name='user-profile'),

    path('add/', views.AddUserExternalTool.as_view(), name='add-user-external-tool'),
    #path('approve_external_tool/', views.ApproveExternalTool.as_view(), name='approve-user-external-tool'),
    path('approve_external_tool/<tool_id>/', views.ApproveExternalTool.as_view(), name='approve-user-external_tool_with_id'),
    path('external_tool_redirect/', views.ExternalToolApproved.as_view(), name='external-tool-approved'),

    # myprofile/myexternaltools/
    path('myexternaltools/',views.ExternalTools.as_view(),name='detail'),

    # myprofile/set_user_default_word_set/
    path('setdefaultwordset/<set_id>/',views.setUserDefaultWordSet,name='set-default-word-set'),
]
