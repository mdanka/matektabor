from django.db import models
from tabor.models import Person, CampGroup


class Camp(models.Model):
	# A tabori csoport.
	group = models.ForeignKey(CampGroup, verbose_name = u'Csoport')

	# A tabor sorszama, nem feltetlenul szam, lehet pl. Extra1 stb.
	number = models.CharField(
		u'Sorsz\u00E1m',
		max_length=200)

	class Meta:
		verbose_name = u'T\u00E1bor'
		verbose_name_plural = u'T\u00E1borok'

	def get_name(self):
		return self.group.name + '/' + self.number

	def __unicode__(self):
		return self.get_name()



class Room(models.Model):
	# A tabor, amelyikhez ez a szoba tartozik.
	camp = models.ForeignKey(Camp, verbose_name = u'T\u00E1bor')

	# Szobaszam/nev, pl.: B, 112 stb.
	name = models.CharField(
		u'Szoban\u00E9v',
		max_length=200)

	# A szoba lakoi.
	people = models.ManyToManyField(Person, blank=True, verbose_name = u'Lak\u00F3k')	

	class Meta:
		verbose_name = u'Szoba'
		verbose_name_plural = u'Szob\u00E1k'

	def get_name(self):
		return self.camp.get_name() + '/' + self.name

	def __unicode__(self):
		return self.get_name()
