from django.urls import path

from . import views

app_name = 'travello'

urlpatterns = [
    path('',views.index, name="index"),
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout")
]
