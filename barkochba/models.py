from django.db import models
from django.forms import ModelForm
from tabor.models import Person



class Story(models.Model):
	# Sorszam a dokumentumban
	order_number = models.PositiveIntegerField(
		u'Sorsz\u00E1m',
		default=0)
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

	def __unicode__(self):
		return self.title

class StoryForm(ModelForm):
	class Meta:
		model = Story
		fields = '__all__'