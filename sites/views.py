# -*- coding: utf-8 -*-
from django.shortcuts import render
from sites.models import Data

def one(request):
    x = Data.objects.filter(site_name="demo_site").order_by("entry_date")
    return render(request, "sites.html", {"list_ob" : x, "site":"demo"})

def two(request):
    x = Data.objects.filter(site_name="abc_site").order_by("entry_date")
    return render(request, "sites.html", {"list_ob" : x, "site":"abc"})

def three(request):
    x = Data.objects.filter(site_name="xyz_site").order_by("entry_date")
    return render(request, "sites.html", {"list_ob" : x, "site":"xyz"})

def sum_entries(site):
    res = []
    x = Data.objects.filter(site_name=site)
    res.append(site.replace("_", " ").upper())
    res.append("{0:.2f}".format(sum(entry.a_value for entry in x)))
    res.append("{0:.2f}".format(sum(entry.b_value for entry in x)))
    return res

def average_entries(site):
    res = []
    x = Data.objects.filter(site_name=site)
    res.append(site.replace("_", " ").upper())
    res.append("{0:.2f}".format(sum(entry.a_value for entry in x)/len(x)))
    res.append("{0:.2f}".format(sum(entry.b_value for entry in x)/len(x)))
    return res

def summary(request):
    res = []
    res.append(sum_entries("demo_site"))
    res.append(sum_entries("abc_site"))
    res.append(sum_entries("xyz_site"))
    return render(request, "summary.html", {"list_ob" : res, "x" : "sum"})

def summary_average(request):
    res = []
    res.append(average_entries("demo_site"))
    res.append(average_entries("abc_site"))
    res.append(average_entries("xyz_site"))
    return render(request, "summary.html", {"list_ob" : res, "x" : "average"})
