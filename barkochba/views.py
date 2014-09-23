import json
from django.shortcuts import render
from django.http import HttpResponse

from tabor.models import Person
from barkochba.models import Story


def main(request):
	story_list = Story.objects.order_by('order_number')
	stories = []
	for story in story_list:
		person_ids = story.people.values_list('id', flat=True)
		person_ids_json = '[' + ', '.join(str(person_id) for person_id in person_ids) + ']'
		story_map = {}
		story_map['story'] = story
		story_map['person_ids_json'] = person_ids_json
		stories.append(story_map)
	context = {
		'stories': stories
	}
	return render(request, 'barkochba/main.html', context)