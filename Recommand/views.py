# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import *

# Create your views here.


@login_required(login_url='/index/')
def list(request,user_id):
    '''
    :param request: 
    :return: une vue ou l'utilisateur aura accès a tout les films qu'il a déja regarder et noter et les films 
    qui lui sont recommandé
    '''
    print(user_id)
    return render(request, 'log.html')
