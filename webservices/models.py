# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Marks(models.Model):
	student= models.CharField(max_length=100, null=True, blank=True)
	subject= models.CharField(max_length=100, null=True, blank=True)
	marks= models.IntegerField(blank=True, null=True, default=0)
	status= models.BooleanField (default=1)
	created= models.DateTimeField(auto_now_add=True)
	class Meta:
		db_table = 'project_marks'


