from django.conf.urls.defaults import *
from codeshare.cab.views.ratings import rate

urlpatterns = patterns('',
    url(r'^(?P<snippet_id>\d+)$', rate, name='cab_snippet_rate'),
)
