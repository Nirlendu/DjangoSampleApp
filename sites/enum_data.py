# -*- coding: utf-8 -*-
from enum import Enum

class Sites(Enum):
	demo = "demo_site"
	abc = "abc_site"
	xyz = "xyz_site"
	summary = "summary"
	summary_average = "summary_average"
	entries_param = "entries"
	site_param = "site"

class Pages(Enum):
	index = "index.html"
	sites = "sites.html"
	summary = "summary.html"
	entries_param = "entries"
	page_param = "page"