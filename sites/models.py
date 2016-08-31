# -*- coding: utf-8 -*-
from django.db import models

class Data(models.Model):
    site_name = models.CharField(max_length=10)
    entry_date = models.DateField()
    a_value = models.DecimalField (default=0, max_digits=5, decimal_places=2)
    b_value = models.DecimalField (default=0, max_digits=5, decimal_places=2)
