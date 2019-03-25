from django.urls import path

from . import views

urlpatterns = [
    path('', views.users, name='all_users'),
    path('^/register', views.register, name='register')
]
