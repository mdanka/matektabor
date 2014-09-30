import json
from django.shortcuts import render
from django.http import HttpResponse, Http404

from tabor.models import Person
from barkochba.models import Story, StoryForm


def main(request):
	all_person_list = Person.objects.all()
	all_person_json = [{'id': int(p.id), 'text': unicode(p.name)} for p in all_person_list]
	all_person_json_string = json.dumps(all_person_json)

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
		'stories': stories,
		'all_people_json': all_person_json_string
	}
	return render(request, 'barkochba/main.html', context)



def story_edit(request, story_id):
	try:
		story = Story.objects.get(id=story_id)
	except Story.DoesNotExist:
		raise Http404

	edit_successful = False
	if request.method == 'POST':
		form = StoryForm(request.POST, instance=story)
		if form.is_valid():
			form.save()
			edit_successful = True
	else:
		form = StoryForm(instance=story)

	context = {
		'story_id': story_id,
		'edit_successful': edit_successful,
		'form': form
	}
	return render(request, 'barkochba/barkochba-form.html', context)