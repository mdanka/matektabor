from django.db import models



class Person(models.Model):
	name = models.CharField(
		u'N\u00E9v',
		max_length=200)



class Story(models.Model):
	# A tortenet rovid cime
	title = models.CharField(
		u'C\u00EDm',
		max_length=200)
	# Maga a tortenet amit elmondunk
	story = models.TextField(
		u'T\u00F6rt\u00E9net')
	# A teljes megoldas
	solution = models.TextField(
		u'Megold\u00E1s')
	# Azok, akik mar hallottak korabban
	people = models.ManyToManyField(Person, blank=True)
