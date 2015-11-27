from django.conf.urls.defaults import *
from django.views.generic.list_detail import object_list
from codeshare.cab.models import Language
from codeshare.cab.views.languages import language_detail

language_info = { 'queryset': Language.objects.all(),
                  'paginate_by': 20 }

urlpatterns = patterns('',
    url(r'^$',
        object_list,
        language_info,
        name='cab_language_list'),
    url(r'^(?P<slug>[-\w]+)/$',
        language_detail,
        name='cab_language_detail'),
)
