# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import *

from django.conf import settings
from django.contrib.auth.models import User


def index(request, **kwargs):
    username = request.POST.get('username', False)
    password = request.POST.get('password', False)
    if username is not False:
        dbuser = User.objects.get(username=username)
        dbuvalid = dbuser.check_password(password)
        print(str(username) + "  +++++++++++  " + str(password))

    user = authenticate(request, username=username, password=password, **kwargs)
    print (str(user))
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'vue.html')


def getout(request):
    logout(request)
    return render(request, 'vue.html')