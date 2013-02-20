from django.conf.urls import patterns, include, url
from django.views.generic.simple import redirect_to

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'codeshare.views.home', name='home'),
    # url(r'^codeshare/', include('codeshare.foo.urls')),
     url(r'^$',redirect_to,{'url':'/home/'}),

    # Uncomment the admin/doc line below to enable admin documentation:
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
    # codeshare
     url(r'^home/',include('codeshare.cab.urls.home')),
     url(r'^snippets/',include('codeshare.cab.urls.snippets')),
     url(r'^languages/',include('codeshare.cab.urls.languages')),
     url(r'^popular/',include('codeshare.cab.urls.popular')),
     url(r'^bookmarks/',include('codeshare.cab.urls.bookmarks')),
     url(r'^ratings/',include('codeshare.cab.urls.ratings')),
)
