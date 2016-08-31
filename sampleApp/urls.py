# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('',
	url(r'^sites/$', 'sites.views.index'),
    url(r'^sites/1$', 'sites.views.demo_site'),
    url(r'^sites/2$', 'sites.views.abc_site'),
    url(r'^sites/3$', 'sites.views.xyz_site'),
    url(r'^summary/$', 'sites.views.summary'),
    url(r'^summary-average/$', 'sites.views.summary_average'),
)
