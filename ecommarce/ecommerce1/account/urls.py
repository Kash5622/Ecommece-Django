from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings


urlpatterns = [
    path('account/login', views.login, name='login'),
    path('account/register', views.register, name='register'),
    path('account/logout', views.logout, name='logout'),
]
