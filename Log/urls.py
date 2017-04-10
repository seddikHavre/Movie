from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^logout/$', views.getout, name='logout'),
    url(r'^log/$', login_required(TemplateView.as_view(template_name='log.html'))),

]
