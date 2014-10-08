from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pumpkin.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^pumpkin/', include('pumpkinpage.urls', namespace="pumpkinpage")),
    url(r'^admin/', include(admin.site.urls)),
)
