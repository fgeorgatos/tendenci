from django.conf.urls.defaults import patterns, url
from tendenci.apps.projects.feeds import LatestEntriesFeed

urlpatterns = patterns('tendenci.apps.projects.views',
    url(r'^projects/$', 'index', name="projects"),
    url(r'^projects/search/$', 'search', name="projects.search"),
    url(r'^projects/feed/$', LatestEntriesFeed(), name='projects.feed'),
    url(r'^projects/(?P<slug>[\w\-\/]+)/$', 'detail', name="projects.detail"),
)