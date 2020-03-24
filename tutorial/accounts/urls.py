from django.contrib import admin
from django.conf.urls import url  
from django.conf import settings
from django.urls import reverse_lazy

from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.views import login_required, logout_then_login
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView
from django.contrib.auth.views import PasswordResetConfirmView
# passwordresetview and password rest done views is used for rendering email page for entering validated email
from django.contrib.auth import views as auth_views
from django.urls import path, include


app_name = 'accounts'

urlpatterns = [
   #url(r'^$',views.home,name="home"),
   path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name="login"),
   path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name="logout"),
   url(r'^register/$',views.register,name='register'),
   url(r'^profile/$',views.view_profile, name='view_profile'),
   url(r'^profile/edit/$',views.edit_profile, name='edit_profile'),
   url(r'^change-password/$', views.change_password, name='change_password'),
   url(r'^reset-password/$', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html', success_url=reverse_lazy('accounts:password_reset_done'),
          email_template_name='accounts/reset_password_email.html'), name='password_reset'),
   url(r'^reset-password/done/$', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),
        name='password_reset_done'),
   url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
       auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html', success_url=reverse_lazy('accounts:password_reset_complete')), name='password_reset_confirm'),
   url(r'^reset-password/complete/$', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),
  ]
