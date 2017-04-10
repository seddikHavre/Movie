# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import *
from django.contrib.auth.decorators import login_required
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
    if user is not None:
        login(request, user)
        return redirect(request.POST.get('next', settings.LOGIN_REDIRECT_URL))
    return render(request, 'vue.html')



def profile(request):
    return render(request, 'log.html')


def getout(request):
    logout(request)
    return render(request, 'log.html')