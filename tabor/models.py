from django.db import models

class Person(models.Model):
	name = models.CharField(
		u'N\u00E9v',
		max_length=200)

	def __unicode__(self):
		return self.name