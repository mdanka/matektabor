import json
from django.shortcuts import render
from django.http import HttpResponse, Http404

from tabor.models import Person
from barkochba.models import Story, StoryForm
from szobabeosztas.models import Camp, Room


def main(request):
	all_person_list = Person.objects.all()
	all_person_json = get_select2_json_for_people(all_person_list)
	all_person_json_string = json.dumps(all_person_json)

	all_camps = Camp.objects.order_by('group__name', 'number')
	camps = []
	for camp in all_camps:
		camp_map = {}
		camp_map['camp'] = camp
		camp_map['camp_name'] = camp.get_name()
		camp_map['rooms'] = Room.objects.filter(camp__id=camp.id)
		camps.append(camp_map)

	all_rooms = Room.objects.all();
	room_list_with_people = []
	for room in all_rooms:
		person_ids = [x for x in room.people.values_list('id', flat=True)];
		room_list_with_people.append({"id": room.id, "person_ids": person_ids})
	rooms_json = json.dumps(room_list_with_people)

	story_list = Story.objects.order_by('order_number')
	stories = []
	storiesWithZeroOrderNumber = []
	for story in story_list:
		person_ids = story.people.values_list('id', flat=True)
		person_ids_json = '[' + ', '.join(str(person_id) for person_id in person_ids) + ']'
		related_person_list = story.people.all()
		related_person_json = get_select2_json_for_people(related_person_list)
		related_person_json_string = json.dumps(related_person_json)
		story_map = {}
		story_map['story'] = story
		story_map['person_ids_json'] = person_ids_json
		story_map['related_people_json'] = related_person_json_string
		if story.order_number == 0:
			storiesWithZeroOrderNumber.append(story_map)
		else:
			stories.append(story_map)
	stories.extend(storiesWithZeroOrderNumber)
	context = {
		'stories': stories,
		'all_people_json': all_person_json_string,
		'camps': camps,
		'rooms_json': rooms_json
	}
	return render(request, 'barkochba/main.html', context)

def story_update_people(request):
	storyId = request.POST.get('storyId')
	people = request.POST.get('people')
	if people == '':
		personIds = []
	else:
		personIds = people.split(',')
	peopleObjects = Person.objects.filter(pk__in = personIds)
	story = Story.objects.get(pk = storyId)
	story.people = peopleObjects
	story.save()
	return HttpResponse()



def get_select2_json_for_people(person_list):
	person_list_json = [{'id': int(p.id), 'text': unicode(p.get_name_with_camp_group())} for p in person_list]
	return person_list_json