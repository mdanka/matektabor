from django.db import models

class Person(models.Model):
	name = models.CharField(
		u'N\u00E9v',
		max_length=200)

	camp_group = models.CharField(
		u'T\u00E1bori csoport',
		max_length=200,
		blank=True,
		default='')

	def get_name_with_camp_group(self):
		if self.camp_group:
			return self.name + ' (' + self.camp_group + ')'
		else:
			return self.name

	def __unicode__(self):
		return self.get_name_with_camp_group()