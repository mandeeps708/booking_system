from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

"""
All the URLs that can be possibly called by user are working here. 
"""

urlpatterns = patterns('',
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'home.views.home', name='home'),
    url(r'^view/', 'home.views.view', name='view'),
    url(r'^cancel/', 'home.views.cancel', name='cancel'),
    url(r'^book/', 'home.views.book', name='book'),
    url(r'^logout/$', 'home.views.logout_view'),
)