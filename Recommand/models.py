# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
# Create your models here.


class Movies(models.Model):
    title = models.CharField(max_length=100)
    genres = models.CharField(max_length=300)
    imdbId = models.CharField(max_length=10)
    mage = models.CharField(max_length=200, blank=True)
    stroyline = models.CharField(max_length=1000, blank=True)
    date = models.CharField(max_length=4, blank=True)
    director = models.CharField(max_length=100, blank=True)

    @classmethod
    def create(cls, t, l, i, s, d, dire):
        m = cls(titre=t, link=l, image=i, stroyline=s, date=d, director=dire)
        return m


class Rate(models.Model):
    movie = models.ForeignKey('Movies', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.FloatField()

    class Meta:
        unique_together = (("movie", "user"),)


class Tag(models.Model):
    tag = models.CharField(max_length=50)


class Relevance(models.Model):
    val = models.FloatField()
    tag = models.ForeignKey('Tag', on_delete=models.CASCADE)
    movie = models.ForeignKey('Movies', on_delete=models.CASCADE)


