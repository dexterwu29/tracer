from django.conf.urls import url, include
from django.contrib import admin
from web.views import account

urlpatterns = [
    url(r'^register/$', account.register, name='register'),
]