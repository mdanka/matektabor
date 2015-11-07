from django.db import models


class CampGroup(models.Model):
	name = models.CharField(
		u'Csoport neve',
		max_length=200)

	class Meta:
		verbose_name = u'T\u00E1bori csoport'
		verbose_name_plural = u'T\u00E1bori csoport'

	def __unicode__(self):
		return self.name


class Person(models.Model):
	name = models.CharField(
		u'N\u00E9v',
		max_length=200)

	# TODO: ehelyett be kellene vezetni egy (nullable) foreign key-t a CampGroup-ra.
	camp_group = models.CharField(
		u'T\u00E1bori csoport',
		max_length=200,
		blank=True,
		default='')

	class Meta:
		verbose_name = u'Szem\u00E9ly'
		verbose_name_plural = u'Szem\u00E9ly'

	def get_name_with_camp_group(self):
		if self.camp_group:
			return self.name + ' (' + self.camp_group + ')'
		else:
			return self.name

	def __unicode__(self):
		return self.get_name_with_camp_group()
