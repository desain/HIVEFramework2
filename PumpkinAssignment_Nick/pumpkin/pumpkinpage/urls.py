from django.conf.urls import patterns, url

from pumpkinpage import views

urlpatterns = patterns('',
                       url(r'^$', views.pumpkin, name="pumpkin"),
                       )