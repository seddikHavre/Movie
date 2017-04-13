from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^index/$', views.index, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
]
