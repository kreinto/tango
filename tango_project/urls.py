from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tango_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^rango/about/', include('about.urls')),
    url(r'^rango/', include('rango.urls')),
)
