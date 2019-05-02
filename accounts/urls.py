#from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views as accounts_views  # views from the accounts app

# all urls start with 'accounts'

urlpatterns = [
    path('signup/', accounts_views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    # the change password urls
    path('settings/password/', auth_views.PasswordChangeView.as_view(template_name='password_change.html'), name='password_change'),
    path('settings/password/done', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'), name='password_change_done'),
]
