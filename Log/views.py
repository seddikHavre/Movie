# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
import django.contrib.auth as auth
from bs4 import BeautifulSoup
from django.http import *
from django.conf import settings
from django.contrib.auth.models import User
import Recommand.models as mod
from django.db.models import Avg
import requests



def CompleteFieldMovie(listMovie):
    '''
    :param listMovie:
    :return: une liste de films, avec tout les champs rempli en utilisant beautifullsoup
    '''
    for item in listMovie:
        lien = "http://www.imdb.com/title/tt" + item.imdbId + "/"
        soup = BeautifulSoup(requests.get(lien).content)
        item.mage = soup.find(itemprop="image")["src"]
        print (item.mage)
        item.stroyline = soup.find(itemprop="description").get_text()
        print(item.stroyline)
        item.director = soup.find(itemprop="director").find(itemprop="name").get_text()
        print(item.director)
        titre = item.title
        item.title = item.title[:-6]
        item.date = titre[len(item.title)+1:-1]
        print(item.date)


def index(request, **kwargs):
    '''
    
    :param request: 
    :param kwargs: 
    :return: si l'utilisateur s'est authentifier alors redirection vers son profils 
             sinon l'utilisateur reste toujour dans la page d'acceuil
             username : cgrant0
             password : zak
             **********************
             username : trichardson1
             password : seddik
             *********************
             username : pellis2
             password : larbi
    '''
    popular = mod.Rate.objects.annotate(average_rating=Avg('rating')).order_by("-average_rating")[0:10]
    listMovie = list()
    for e in popular:
        movie = mod.Movies.objects.get(pk=e.movie_id)
        listMovie.insert(len(listMovie), movie)
    CompleteFieldMovie(listMovie)
    username = request.POST.get('username', False) # récupération d'username depuis le form sur la vue
    password = request.POST.get('password', False) # récupératiion du mot de passe depuis le form.
    if username is not False: # juste pour tester
        dbuser = User.objects.get(username=username)
        dbuvalid = dbuser.check_password(password)
        #dbuser.set_password("seddik")
        #dbuser.save(update_fields=["password"])
        print(str(username) + "  +++++++++++  " + str(password))

    user = auth.authenticate(request, username=username, password=password,**kwargs)
    if user is not None:
        auth.login(request, user)
        request.session['user']=user.id
        return HttpResponseRedirect(reverse('list'))
        #return redirect('list', args=[user.id])

    if request.user.is_authenticated(): # tester si l'utilisateur s'est connecter ou pas
        print("logged !!! ")
    return render(request, 'vue.html', {'list': listMovie})


def logout(request):
    '''
    
    :param request: 
    :return: une fois l'utlisateur s'est deconnecter, redirection vers la page d'acceuil
    '''
    auth.logout(request)
    return HttpResponseRedirect(settings.LOGIN_URL)