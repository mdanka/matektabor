from django.shortcuts import get_object_or_404, render

from szobabeosztas.models import Camp, Room
from barkochba.models import Story

def try_parse_int(s, default_val=-1):
  try:
    return int(s)
  except ValueError:
    return default_val

def index(request):
	camp_list = Camp.objects.order_by('group__name', 'number')
	context = {'camp_list': camp_list}
	return render(request, 'export/index.html', context)

def camp_export(request, camp_id):
	camp = get_object_or_404(Camp, pk=camp_id)
	rooms = camp.room_set.all()
	requested_room_ids = [try_parse_int(s) for s in request.GET.getlist('room')]
	if requested_room_ids:
		rooms = camp.room_set.filter(id__in=requested_room_ids)
	include_descriptions = request.GET.get('description', '0') == '1'
	include_solutions = request.GET.get('solution', '0') == '1'
	story_list = Story.objects.order_by('order_number')
	stories = []
	storiesWithZeroOrderNumber = []
	for story in story_list:
		story_map = {}
		story_map['story'] = story
		story_map['people'] = story.people.all()
		story_map['rooms'] = []
		for room in rooms:
			room_people_ids = room.people.all().values('id')
			people = story.people.filter(id__in=room_people_ids).order_by('name')
			if (not people):
				continue
			room_map = {}
			room_map['room'] = room.name
			room_map['people'] = people
			story_map['rooms'].append(room_map)
		if story.order_number == 0:
			storiesWithZeroOrderNumber.append(story_map)
		else:
			stories.append(story_map)
	stories.extend(storiesWithZeroOrderNumber)
	context = {
		'stories': stories,
		'camp': camp,
		'include_descriptions': include_descriptions,
		'include_solutions': include_solutions
	}
	return render(request, 'export/camp_export.html', context)


