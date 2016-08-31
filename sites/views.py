# -*- coding: utf-8 -*-
from django.shortcuts import render
from sites.models import Data
from django.db import connection
from enum_data import Sites, Pages

def index(request):
	return render(request, Pages.index, {})

def demo_site(request):
	x = Data.objects.filter(site_name = Sites.demo).order_by("entry_date")
	return render(request, Pages.sites, {"entries" : x, "site" : Sites.demo})

def abc_site(request):
	x = Data.objects.filter(site_name = Sites.abc).order_by("entry_date")
	return render(request, Pages.sites, {"entries" : x, "site" : Sites.abc})

def xyz_site(request):
	x = Data.objects.filter(site_name = Sites.xyz).order_by("entry_date")
	return render(request, Pages.sites, {"entries" : x, "site" : Sites.xyz})

def sum_entries(site):
	res = []
	res.append(site.replace("_", " ").upper())
	cursor = connection.cursor()
	cursor.execute("SELECT SUM(a_value) from sites_data where site_name = '" + site + "'")
	for p in cursor.fetchone():
		res.append(p)
	cursor.execute("SELECT SUM(b_value) from sites_data where site_name = '" + site + "'")
	for p in cursor.fetchone():
		res.append(p)
	return res

def average_entries(site):
	res = []
	x = Data.objects.filter(site_name = site)
	res.append(site.replace("_", " ").upper())
	res.append("{0:.2f}".format(sum(entry.a_value for entry in x)/len(x)))
	res.append("{0:.2f}".format(sum(entry.b_value for entry in x)/len(x)))
	return res

def summary(request):
	res = []
	res.append(sum_entries(Sites.demo))
	res.append(sum_entries(Sites.abc))
	res.append(sum_entries(Sites.xyz))
	return render(request, Pages.summary, {"entries" : res, "page" : Sites.summary})

def summary_average(request):
	res = []
	res.append(average_entries(Sites.demo))
	res.append(average_entries(Sites.abc))
	res.append(average_entries(Sites.xyz))
	return render(request, Pages.summary, {"entries" : res, "page" : Sites.summary_average})
