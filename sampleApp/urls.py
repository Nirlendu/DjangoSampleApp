from django.conf.urls import patterns, url

urlpatterns = patterns('',
	url(r'^sites/$', 'sites.views.index'),
    url(r'^sites/1', 'sites.views.one'),
    url(r'^sites/2', 'sites.views.two'),
    url(r'^sites/3', 'sites.views.three'),
    url(r'^summary/', 'sites.views.summary'),
    url(r'^summary-average/', 'sites.views.summary_average'),
)
