from django.conf.urls import patterns, include, url
from django.views.generic.simple import redirect_to
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$',redirect_to, {'url': '/accounts/signin/'}),
    # url(r'^graduate/', include('graduate.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^accounts/', include('userena.urls')),  
    url(r'^article/categories/',include('graduate.coltrane.urls.categories')),
    url(r'^article/entries/',include('graduate.coltrane.urls.entries')),
)
