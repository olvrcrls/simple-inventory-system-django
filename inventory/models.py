from __future__ import unicode_literals

from django.db import models

# Create your models here that will represent as fields on the database.
class Item(models.Model):
	title = models.CharField(max_length=200) # column 1
	description = models.TextField() # column 2
	amount = models.IntegerField() # column 3