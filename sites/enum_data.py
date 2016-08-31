# -*- coding: utf-8 -*-
from enum import Enum

class Sites(Enum):
	demo = "demo_site"
	abc = "abc_site"
	xyz = "xyz_site"
	summary = "summary"
	summary_average = "summary_average"

class Pages(Enum):
	index = "index.html"
	sites = "sites.html"
	summary = "summary.html"