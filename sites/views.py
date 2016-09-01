# -*- coding: utf-8 -*-
from django.shortcuts import render
from sites.models import Data
from django.db import connection
from enum_data import Sites, Pages

def index(request):
	return render(request, Pages.index, {})

def demo_site(request):
	entries = Data.objects.filter(site_name = Sites.demo).order_by("entry_date")
	return render(request, Pages.sites, {Sites.entries_param : entries, Sites.site_param : Sites.demo})

def abc_site(request):
	entries = Data.objects.filter(site_name = Sites.abc).order_by("entry_date")
	return render(request, Pages.sites, {Sites.entries_param : entries, Sites.site_param : Sites.abc})

def xyz_site(request):
	entries = Data.objects.filter(site_name = Sites.xyz).order_by("entry_date")
	return render(request, Pages.sites, {Sites.entries_param : entries, Sites.site_param : Sites.xyz})

def sum_entries(site):
	entries = []
	entries.append(site.replace("_", " ").upper())
	cursor = connection.cursor()
	cursor.execute("SELECT SUM(a_value) from sites_data where site_name = '" + site + "'")
	for p in cursor.fetchone():
		entries.append(p)
	cursor.execute("SELECT SUM(b_value) from sites_data where site_name = '" + site + "'")
	for p in cursor.fetchone():
		entries.append(p)
	return entries

def average_entries(site):
	entries = []
	entry = Data.objects.filter(site_name = site)
	entries.append(site.replace("_", " ").upper())
	entries.append("{0:.2f}".format(sum(x.a_value for x in entry)/len(entry)))
	entries.append("{0:.2f}".format(sum(x.b_value for x in entry)/len(entry)))
	return entries

def summary(request):
	aggregate = []
	aggregate.append(sum_entries(Sites.demo))
	aggregate.append(sum_entries(Sites.abc))
	aggregate.append(sum_entries(Sites.xyz))
	return render(request, Pages.summary, {Pages.entries_param : aggregate, Pages.page_param: Sites.summary})

def summary_average(request):
	aggregate = []
	aggregate.append(average_entries(Sites.demo))
	aggregate.append(average_entries(Sites.abc))
	aggregate.append(average_entries(Sites.xyz))
	return render(request, Pages.summary, {Pages.entries_param : aggregate, Pages.page_param : Sites.summary_average})
