from django.conf.urls.defaults import *

from coltrane.models import Entry
from graduate.coltrane.views import recommend_article
from django.views.generic.list_detail import object_list

entry_info_dict = {
    'queryset': Entry.live.all(),
    'date_field': 'pub_date',
}


urlpatterns = patterns('graduate.coltrane.generic.date_based',
    (r'^last/$', 'archive_index', entry_info_dict, 'coltrane_entry_archive_index'),
    (r'^(?P<year>\d{4})/$', 'archive_year', entry_info_dict, 'coltrane_entry_archive_year'),
    (r'^(?P<year>\d{4})/(?P<month>\w{3})/$', 'archive_month', entry_info_dict, 'coltrane_entry_archive_month'),
    (r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/$', 'archive_day', entry_info_dict, 'coltrane_entry_archive_day'),
    (r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', 'object_detail', entry_info_dict, 'coltrane_entry_detail'),
)

urlpatterns += patterns('',
    url(r'^$',object_list,{'queryset': Entry.live.all()},'coltrane_entry_index'),
    url(r'^recommend/$',recommend_article,name='recommend_article'),
)
