from django.contrib import admin
from django.urls import path,include
from allauth.account.views import SignupView, LoginView, PasswordResetView,TemplateView

class MySignupView(SignupView):
    template_name = 'signup.html'

class MyLoginView(LoginView):
    template_name = 'login.html'

class MyPasswordResetView(PasswordResetView):
    template_name = 'password_reset.html'

class PrivacyPolicy(TemplateView):
    template_name = 'privacy-policy.html'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('words/',include('words.urls')),
    #main path is to words
    path('',include('words.urls')),
    path('myprofile/',include('myprofile.urls')),
    path('accounts/login/',MyLoginView.as_view(),name='account_login'),
    path('accounts/',include('allauth.urls')),
    path('privacy_policy/',PrivacyPolicy.as_view(),name='privacy_policy'),


]
