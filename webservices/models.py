# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Students(models.Model):
	name= models.CharField(max_length=100, null=True, blank=True)
	status= models.BooleanField (default=1)
	created= models.DateTimeField(auto_now_add=True)
	class Meta:
		db_table = 'project_students'

class Subjects(models.Model):
	name= models.CharField(max_length=100, null=True, blank=True)
	status= models.BooleanField (default=1)
	created= models.DateTimeField(auto_now_add=True)
	class Meta:
		db_table = 'project_subjects'

class Marks(models.Model):
	student= models.ForeignKey(Students,on_delete=models.CASCADE,blank=True, null=True)
	subject= models.ForeignKey(Subjects,on_delete=models.CASCADE,blank=True, null=True)
	marks= models.IntegerField(blank=True, null=True, default=0)
	status= models.BooleanField (default=1)
	created= models.DateTimeField(auto_now_add=True)
	class Meta:
		db_table = 'project_marks'

