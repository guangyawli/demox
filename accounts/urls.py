"""demox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from accounts.views import index, UserLoginAPI2, sign_in, log_out, my_profile, apply_to, activate_master, send_apply, \
    apply_master

urlpatterns = [
    path('', index, name='account_home'),
    # path('register/', sign_up, name='Register'),
    path('login/', sign_in, name='Login'),
    path('rlogin/', UserLoginAPI2, name='rlogin'),
    path('logout/', log_out, name='Logout'),
    path('profile/', my_profile, name='my_profile'),
    path('applyto/', apply_to, name='apply_to'),
    path('send_apply/', send_apply, name='send_apply'),
    path('activate/<str:active_key>/<str:token>/', activate_master, name='activate_master'),
    path('apply_master/<str:active_key>/<str:token>/', apply_master, name='apply_master'),

    # path('reset_request/', request_reset, name='request_reset'),
    # path('reset_password/<str:active_key>/<str:token>/', reset_user, name='reset_user'),
    # path('resend_confirm/', resend_active_letter, name='resend_active_letter'),
]
